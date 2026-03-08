import sys

from interfaz_servicio_suma.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b, c, d, e):
        self.req.a = a
        self.req.b = b
        self.req.c = c
        self.req.d = d
        self.req.e = e
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    if len(sys.argv) != 6:
        print("Usage: ros2 run servicio_suma client a b c d e")
        return

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])
    e = int(sys.argv[5])

    minimal_client = MinimalClientAsync()
    future = minimal_client.send_request(a, b, c, d, e)
    rclpy.spin_until_future_complete(minimal_client, future)

    response = future.result()
    minimal_client.get_logger().info(
        'Result: %d + %d - %d * %d / %d = %.6f' %
        (a, b, c, d, e, response.result))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
    
    
    
    
    