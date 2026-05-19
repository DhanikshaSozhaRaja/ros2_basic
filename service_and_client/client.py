import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddClient(Node):

	def __init__(self):
		super().__init__('add_client')
		
		self.client = self.create_client(
			AddTwoInts,
			'add_two_ints'
		)
		
		while not self.client.wait_for_service(timeout_sec = 1.0):
			self.get_logger().info('Service not available')
		self.req = AddTwoInts.Request()
		
	def send_request(self, a , b):
		self.req.a = a
		self.req.b = b
		
		future = self.client.call_async(self.req)
		
		rclpy.spin_until_future_complete(self, future)
		
		return future.result()
		
def main(args=None):
	rclpy.init(args=args)
	client = AddClient()
	response = client.send_request(5,3)
	print("Result:", response.sum)
	rclpy.shutdown()

if __name__ == '__main__':
	main()
