import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelPublisher(Node):
    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.tick)  # 10 Hz

    def tick(self):
        msg = Twist()
        msg.linear.x = 0.2      # anda sempre
        msg.angular.z = 0.0
        self.pub.publish(msg)
        self.get_logger().info(
            f'cmd_vel -> linear.x={msg.linear.x:.2f} angular.z={msg.angular.z:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

