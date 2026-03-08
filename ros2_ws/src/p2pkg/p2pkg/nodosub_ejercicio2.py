#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from interfaz.msg import P2pkgMensaje


class NodoSubEjercicio2(Node):
    def __init__(self):
        super().__init__('nodosub_ejercicio2')
        self.subscription = self.create_subscription(
            P2pkgMensaje,
            '/topic_ejercicio2',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f"[SUB] fecha={msg.fecha} numero={msg.numero} "
            f"x={msg.posicion.position.x:.3f} w={msg.posicion.orientation.w:.3f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = NodoSubEjercicio2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()