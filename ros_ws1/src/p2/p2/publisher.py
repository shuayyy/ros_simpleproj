import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.declare_parameter('topic',value = 'talker_topic')
        topic_name= self.get_parameter('topic').get_parameter_value().string_value
                                       
        self.publisher = self.create_publisher(String, topic_name, 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.message_count = 0

    def publish_message(self):
        msg = String()
        msg.data = 'Message number %d' % self.message_count
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.message_count += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
