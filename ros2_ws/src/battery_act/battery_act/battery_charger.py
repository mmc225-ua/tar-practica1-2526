#!/usr/bin/env python3
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse

from interfaz_battery_act.action import Battery


class BatteryCharger(Node):

    def __init__(self):
        super().__init__('battery_charger')

        self._action_server = ActionServer(
            self,
            Battery,
            'battery',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )

        self.get_logger().info("Action server '/battery' listo.")

    def goal_callback(self, goal_request):
        # Validación simple del goal
        target = goal_request.target_percentage
        if target < 0 or target > 100:
            self.get_logger().warn(f"Goal rechazado: target_percentage fuera de rango: {target}")
            return GoalResponse.REJECT

        self.get_logger().info(f"Goal recibido: target_percentage={target}")
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info("Solicitud de cancelación recibida. Aceptando cancelación.")
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        target = goal_handle.request.target_percentage
        self.get_logger().info(f"Ejecutando descarga hasta {target}% ...")

        feedback = Battery.Feedback()
        result = Battery.Result()

        current = 100

        while current > target:
            # Si el cliente solicita cancelación
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                result.warning = "Acción cancelada por el cliente."
                self.get_logger().info(result.warning)
                return result

            # Actualiza batería
            current -= 5
            if current < 0:
                current = 0

            feedback.current_percentage = current
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f"Feedback: current_percentage={current}%")

            time.sleep(1)

        # Termina con éxito
        goal_handle.succeed()
        result.warning = "Batería baja, por favor cargue el robot!"
        self.get_logger().info("Objetivo alcanzado. Enviando result.")
        return result


def main(args=None):
    rclpy.init(args=args)
    node = BatteryCharger()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
