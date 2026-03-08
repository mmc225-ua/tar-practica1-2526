#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node

from interfaz_service_temp.srv import TemperatureConvert


class TempConvertClient(Node):
    def __init__(self):
        super().__init__('temp_convert_client')
        self.cli = self.create_client(TemperatureConvert, 'convert_temperature')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servicio no disponible, esperando...')

        self.req = TemperatureConvert.Request()

    def send_request(self, value, conv_type):
        self.req.input_temp = float(value)
        self.req.conversion_type = conv_type
        return self.cli.call_async(self.req)


def main(args=None):
    if len(sys.argv) != 3:
        print("Uso: ros2 run service_temp client <temp> <Cel_to_Far|Far_to_Cel>")
        return

    temp_value = sys.argv[1]
    conv_type = sys.argv[2]

    rclpy.init(args=args)
    node = TempConvertClient()
    future = node.send_request(temp_value, conv_type)
    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        node.get_logger().info(
            f"Resultado: {temp_value} ({conv_type}) -> {future.result().converted_temp}"
        )
    else:
        node.get_logger().error("Fallo en la llamada al servicio")

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
