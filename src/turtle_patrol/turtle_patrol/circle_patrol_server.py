#!/usr/bin/env python3

import math
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

from turtle_patrol.action import ExecuteCircle


class CirclePatrolServer(Node):

    def __init__(self):
        super().__init__('circle_patrol_server')

        self.current_pose = None

        self.cmd_pub = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.pose_sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        self.action_server = ActionServer(
            self,
            ExecuteCircle,
            'execute_circle',
            self.execute_callback
        )

        self.get_logger().info(
            'Circle Patrol Action Server Started'
        )

    def pose_callback(self, msg):
        self.current_pose = msg

    def near_wall(self):

        if self.current_pose is None:
            return False

        x = self.current_pose.x
        y = self.current_pose.y

        return (
            x < 1.0 or
            x > 10.0 or
            y < 1.0 or
            y > 10.0
        )

    async def execute_callback(self, goal_handle):

        radius = goal_handle.request.radius

        if radius <= 0.0:

            goal_handle.abort()

            result = ExecuteCircle.Result()
            result.success = False
            result.final_report = 'Invalid radius'

            return result

        linear_velocity = 1.5
        angular_velocity = linear_velocity / radius

        twist = Twist()
        twist.linear.x = linear_velocity
        twist.angular.z = angular_velocity

        while self.current_pose is None:
            time.sleep(0.1)

        start_x = self.current_pose.x
        start_y = self.current_pose.y

        total_distance = 0.0

        feedback_msg = ExecuteCircle.Feedback()

        self.get_logger().info(
            f'Starting patrol with radius {radius}'
        )

        while rclpy.ok():

            if self.near_wall():

                stop_msg = Twist()
                self.cmd_pub.publish(stop_msg)

                goal_handle.abort()

                result = ExecuteCircle.Result()
                result.success = False
                result.final_report = (
                    'Mission Aborted: Boundary Collision Imminent!'
                )

                self.get_logger().warn(
                    result.final_report
                )

                return result

            self.cmd_pub.publish(twist)

            total_distance += linear_velocity * 0.1

            feedback_msg.distance_traveled = total_distance
            feedback_msg.current_status = "Patrolling..."

            goal_handle.publish_feedback(
                feedback_msg
            )

            current_x = self.current_pose.x
            current_y = self.current_pose.y

            distance_from_start = math.sqrt(
                (current_x - start_x) ** 2 +
                (current_y - start_y) ** 2
            )

            circumference = (
                2 * math.pi * radius
            )

            if (
                total_distance >= circumference - 0.5
                and
                distance_from_start < 0.2
            ):
                break

            time.sleep(0.1)

        stop_msg = Twist()
        self.cmd_pub.publish(stop_msg)

        goal_handle.succeed()

        result = ExecuteCircle.Result()
        result.success = True
        result.final_report = (
            'Circle patrol completed successfully'
        )

        self.get_logger().info(
            result.final_report
        )

        return result


def main(args=None):

    rclpy.init(args=args)

    node = CirclePatrolServer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
