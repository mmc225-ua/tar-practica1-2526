#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String

from interfaz.action import EjFibonacci


class EjFibonacciActionClient(Node):

    def __init__(self):
        super().__init__('ej_fibonacci_action_client')

        # Parámetro ROS2 para el orden (por defecto 10; si tu enunciado pide otro, lo cambias aquí)
        self.declare_parameter('orden', 10)
        self.orden = int(self.get_parameter('orden').value)

        # Publisher del estado
        self.estado_pub = self.create_publisher(String, '/estado_accion', 10)

        # Action client
        self._action_client = ActionClient(self, EjFibonacci, 'ej_fibonacci')

        # Timer para publicar "en proceso" mientras no termine
        self._en_proceso = False
        self.timer = self.create_timer(0.5, self.publicar_estado)

    def publicar_estado(self):
        if self._en_proceso:
            msg = String()
            msg.data = "en proceso"
            self.estado_pub.publish(msg)

    def send_goal(self):
        goal_msg = EjFibonacci.Goal()
        goal_msg.orden = self.orden

        self.get_logger().info(f'Enviando goal con orden={self.orden}...')
        self._action_client.wait_for_server()

        self._en_proceso = True
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rechazado :(')
            self._en_proceso = False
            rclpy.shutdown()
            return

        self.get_logger().info('Goal aceptado :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self._en_proceso = False
        self.get_logger().info(f'Resultado secuencia_final: {result.secuencia_final}')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        # El feedback es float64, lo mostramos
        self.get_logger().info(f'Feedback recibido (sqrt(mean)): {feedback.feedback}')


def main(args=None):
    rclpy.init(args=args)
    node = EjFibonacciActionClient()
    node.send_goal()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
