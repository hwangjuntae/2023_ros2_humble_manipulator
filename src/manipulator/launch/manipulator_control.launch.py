import launch
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_path = "/home/teus/ros2_ws/src/manipulator/urdf/manipulator.urdf"
    config_path = get_package_share_directory('manipulator') + '/config/control.yaml'

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        arguments=[urdf_path]
    )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen',
        parameters=[{'yaml_file': config_path}],
        remappings=[('/joint_states', '/robot/joint_states')],
        arguments=['--ros-args', '-r', '__node:=joint_state_publisher_gui', '-r', '/joint_states:=/robot/joint_states']
    )

    return launch.LaunchDescription([
        robot_state_publisher,
        joint_state_publisher_gui
    ])
