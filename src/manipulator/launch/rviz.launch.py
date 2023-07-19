import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        # Start joint_state_publisher
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            parameters=[{'use_gui': False}],
            output='screen'
        ),

        # Start robot_state_publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open('/home/teus/ros2_ws/src/manipulator/urdf/manipulator.urdf').read()}],
            output='screen'
        ),

        # Start rviz2
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', '/home/teus/ros2_ws/src/manipulator/rviz/rviz_config.rviz'],
            output='screen'
        )
    ])
