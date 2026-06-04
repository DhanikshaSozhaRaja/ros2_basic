import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
	def __init__(self):
		super().__init__('py_publisher')
		self.publisher_=self.create_publisher(String, 'topic_py', 10)
		self.timer=self.create_timer(1.0, self.publish_message)
	def publish_message(self):
		msg = String()
		msg.data = "'Hello!' from Python"

		self.get_logger().info(f'Publishing: {msg.data}')

		self.publisher_.publish(msg)

def main(args=None):
	rclpy.init(args=args)
	node = PublisherNode()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()
