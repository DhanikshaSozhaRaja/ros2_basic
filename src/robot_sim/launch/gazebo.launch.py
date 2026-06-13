from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

import os
import xacro

from ament_index_python.packages import \
get_package_share_directory


def generate_launch_description():

    pkg = get_package_share_directory(
        'robot_sim'
    )

    world = os.path.join(
        pkg,
        'worlds',
        'custom_world.sdf'
    )

    xacro_file = os.path.join(
        pkg,
        'urdf',
        'robot.urdf.xacro'
    )

    robot_desc = xacro.process_file(
        xacro_file
    ).toxml()

    gazebo = ExecuteProcess(
        cmd=[
            'ign',
            'gazebo',
            world,
            '-r'
        ],
        output='screen'
    )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {
                'robot_description':
                robot_desc
            }
        ]
    )

    return LaunchDescription([
        gazebo,
        rsp
    ])

