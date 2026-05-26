#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from rclpy.action import ActionClient

from turtle_patrol.action import ExecuteCircle


class CirclePatrolClient(Node):

    def __init__(self):
        super().__init__('circle_patrol_client')

        self.client = ActionClient(
            self,
            ExecuteCircle,
            'execute_circle'
        )

    def send_goal(self):

        goal_msg = ExecuteCircle.Goal()
        goal_msg.radius = 3.0

        self.client.wait_for_server()

        self.send_goal_future = self.client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        self.send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        self.result_future = goal_handle.get_result_async()

        self.result_future.add_done_callback(
            self.result_callback
        )

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f'Distance Travelled: '
            f'{feedback.distance_traveled:.2f}'
        )

    def result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            f'Success: {result.success}'
        )

        self.get_logger().info(
            f'Report: {result.final_report}'
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    node = CirclePatrolClient()

    node.send_goal()

    rclpy.spin(node)


if __name__ == '__main__':
    main()

