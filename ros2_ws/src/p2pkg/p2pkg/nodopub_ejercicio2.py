#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from random import random
from datetime import date

from interfaz.msg import P2pkgMensaje


class NodoPubEjercicio2(Node):
    def __init__(self):
        super().__init__('nodopub_ejercicio2')

        # Parámetro ROS2 estándar (por defecto 5)
        self.declare_parameter('numero', 5)
        self.numero = int(self.get_parameter('numero').value)

        self.publisher_ = self.create_publisher(P2pkgMensaje, '/topic_ejercicio2', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = P2pkgMensaje()

        # Campo numero
        msg.numero = self.numero

        # Fecha actual
        msg.fecha = date.today().isoformat()

        # Pose aleatoria (position y orientation)
        msg.posicion.position.x = random()
        msg.posicion.position.y = random()
        msg.posicion.position.z = random()

        msg.posicion.orientation.x = random()
        msg.posicion.orientation.y = random()
        msg.posicion.orientation.z = random()
        msg.posicion.orientation.w = random()

        self.publisher_.publish(msg)

        self.get_logger().info(
            f"[PUB] fecha={msg.fecha} numero={msg.numero} "
            f"x={msg.posicion.position.x:.3f} w={msg.posicion.orientation.w:.3f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = NodoPubEjercicio2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()