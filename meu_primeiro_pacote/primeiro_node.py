import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PrimeiroNode(Node):

    def __init__(self):
        super().__init__('primeiro_node')
        self.publisher_ = self.create_publisher(String, 'topico_teste', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Olá ROS 2!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PrimeiroNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
