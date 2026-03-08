#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from interfaz_battery_act.action import Battery


class BatteryClient(Node):

    def __init__(self, target):
        super().__init__('battery_client')
        self._action_client = ActionClient(self, Battery, 'battery')
        self._goal_handle = None
        self._result_future = None
        self._target = target

    def send_goal(self):
        goal_msg = Battery.Goal()
        goal_msg.target_percentage = self._target

        self.get_logger().info(f"Esperando servidor de acción '/battery'...")
        self._action_client.wait_for_server()

        self.get_logger().info(f"Enviando goal: target_percentage={self._target}")
        send_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        send_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        self._goal_handle = future.result()
        if not self._goal_handle.accepted:
            self.get_logger().info("Goal rechazado :(")
            rclpy.shutdown()
            return

        self.get_logger().info("Goal aceptado :)")
        self._result_future = self._goal_handle.get_result_async()
        self._result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        fb = feedback_msg.feedback
        self.get_logger().info(f"Feedback recibido: current_percentage={fb.current_percentage}%")

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"RESULT: {result.warning}")
        rclpy.shutdown()

    def cancel_goal(self):
        if self._goal_handle is None:
            self.get_logger().warn("No hay goal_handle todavía, no puedo cancelar.")
            return
        self.get_logger().warn("Enviando solicitud de cancelación...")
        cancel_future = self._goal_handle.cancel_goal_async()
        cancel_future.add_done_callback(self.cancel_done)

    def cancel_done(self, future):
        cancel_response = future.result()
        self.get_logger().warn(f"Cancelación solicitada. Respuesta: {cancel_response}")


def main(args=None):
    if len(sys.argv) != 2:
        print("Uso: ros2 run battery_act battery_client <target_percentage>")
        return

    target = int(sys.argv[1])

    rclpy.init(args=args)
    node = BatteryClient(target)
    node.send_goal()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Ctrl+C = cancelar goal (cumple el requisito de cancelación)
        node.cancel_goal()
        # damos un poco de tiempo para que el cancel viaje
        rclpy.spin_once(node, timeout_sec=1.0)
        rclpy.shutdown()


if __name__ == '__main__':
    main()
