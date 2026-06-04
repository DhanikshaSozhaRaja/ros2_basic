from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os
import xacro


def generate_launch_description():

    pkg_path = get_package_share_directory('robot_simulation')

    world_file = os.path.join(
        pkg_path,
        'worlds',
        'custom_world.sdf'
    )

    xacro_file = os.path.join(
        pkg_path,
        'urdf',
        'robot.urdf.xacro'
    )

    robot_description = xacro.process_file(
        xacro_file
    ).toxml()

    return LaunchDescription([

        ExecuteProcess(
            cmd=[
                'ros2',
                'run',
                'ros_gz_sim',
                'gz_sim',
                world_file
            ],
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[
                {
                    'robot_description':
                    robot_description
                }
            ]
        ),

    ])
