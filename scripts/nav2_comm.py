#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseWithCovariance
from std_msgs.msg import String
from std_msgs.msg import Header


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.pose_pub_ = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 10)
        # timer_period = 0.5  # seconds
        # self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.publish()

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    def publish(self):
        pose_stamp_msg = PoseWithCovarianceStamped()
        header_msg = Header()
        header_msg.stamp = self.get_clock().now().to_msg()
        header_msg.frame_id = "map"
        pose_msg = PoseWithCovariance()
        pose_msg.pose.position.x = -2.0
        pose_msg.pose.position.y = -0.5
        pose_msg.pose.position.z = 0.0
        pose_stamp_msg.header = header_msg
        pose_stamp_msg.pose = pose_msg
        self.pose_pub_.publish(pose_stamp_msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
