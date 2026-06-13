from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

import os
import xacro
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg = get_package_share_directory('robot_sim')

    world = os.path.join(pkg, 'worlds', 'custom_world.sdf')

    xacro_file = os.path.join(pkg, 'urdf', 'robot.urdf.xacro')

    robot_desc = xacro.process_file(xacro_file).toxml()

    # ---------------- GAZEBO ----------------
    gazebo = ExecuteProcess(
        cmd=['ign', 'gazebo', world, '-r'],
        output='screen'
    )

    # ---------------- ROBOT STATE PUBLISHER ----------------
    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}],
        output='screen'
    )

    # ---------------- JOINT STATE PUBLISHER (OPTIONAL) ----------------
    joint_state_pub = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen'
    )

    # ---------------- SPAWN ROBOT INTO GAZEBO ----------------
    spawn = ExecuteProcess(
        cmd=[
            'ros2', 'run', 'ros_gz_sim', 'create',
            '-name', 'robot_sim',
            '-topic', 'robot_description'
        ],
        output='screen'
    )

    # ---------------- ROS2 CONTROL NODE ----------------
    
    # ---------------- CONTROLLER SPAWN ----------------
    load_joint_state = ExecuteProcess(
        cmd=[
            'ros2', 'control', 'load_controller',
            '--set-state', 'active',
            'joint_state_broadcaster'
        ],
        output='screen'
    )
    joint_state_broadcaster = Node(
    package='controller_manager',
    executable='spawner',
    arguments=['joint_state_broadcaster']
)

    diff_drive_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['diff_drive_controller']
)

    arm_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['arm_controller']
)
    load_diff_drive = ExecuteProcess(
        cmd=[
            'ros2', 'control', 'load_controller',
            '--set-state', 'active',
            'diff_drive_controller'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        rsp,
        joint_state_pub,
        spawn,
        diff_drive_controller,
        arm_controller,
        joint_state_broadcaster,
        load_joint_state,
        load_diff_drive
    ])

