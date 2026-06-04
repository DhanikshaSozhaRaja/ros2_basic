import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddService(Node):
	def __init__(self):
		super().__init__('add_service')
		
		self.srv = self.create_service(
			AddTwoInts,
			'add_two_ints',
			self.add_callback
		)
	def add_callback(self, request, response):
		response.sum = request.a + request.b
		self.get_logger().info(f"Incoming request: {request.a} +{request.b}")
		return response

def main(args=None):
	rclpy.init(args=args)
	
	node = AddService()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()
			
