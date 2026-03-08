#!/usr/bin/env python3
import time
import math

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from interfaz.action import EjFibonacci


class EjFibonacciActionServer(Node):

    def __init__(self):
        super().__init__('ej_fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            EjFibonacci,
            'ej_fibonacci',
            self.execute_callback
        )

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing EjFibonacci goal...')

        feedback_msg = EjFibonacci.Feedback()

        # Secuencia inicial
        secuencia = [0, 1]

        # Publicamos feedback inicial
        media = sum(secuencia) / float(len(secuencia))
        feedback_msg.feedback = math.sqrt(media)
        goal_handle.publish_feedback(feedback_msg)
        self.get_logger().info(f'Feedback sqrt(mean): {feedback_msg.feedback}')
        time.sleep(1)

        # Construimos la secuencia hasta "orden"
        for i in range(1, goal_handle.request.orden):
            secuencia.append(secuencia[i] + secuencia[i - 1])

            media = sum(secuencia) / float(len(secuencia))
            feedback_msg.feedback = math.sqrt(media)

            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'Feedback sqrt(mean): {feedback_msg.feedback}')
            time.sleep(1)

        goal_handle.succeed()

        result = EjFibonacci.Result()
        result.secuencia_final = secuencia
        return result


def main(args=None):
    rclpy.init(args=args)
    node = EjFibonacciActionServer()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
