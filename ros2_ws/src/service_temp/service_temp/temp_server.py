#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from interfaz_service_temp.srv import TemperatureConvert


class TempConvertServer(Node):
    def __init__(self):
        super().__init__('temp_convert_server')
        self.srv = self.create_service(
            TemperatureConvert,
            'convert_temperature',
            self.callback
        )
        self.get_logger().info("Servicio 'convert_temperature' listo.")

    def callback(self, request, response):
        t = request.input_temp
        conv = request.conversion_type

        if conv == "Cel_to_Far":
            response.converted_temp = (t * 9.0 / 5.0) + 32.0
        elif conv == "Far_to_Cel":
            response.converted_temp = (t - 32.0) * 5.0 / 9.0
        else:
            self.get_logger().warn("conversion_type invalido. Usa Cel_to_Far o Far_to_Cel")
            response.converted_temp = float('nan')

        self.get_logger().info(f"Req: {t} ({conv}) -> Resp: {response.converted_temp}")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = TempConvertServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
