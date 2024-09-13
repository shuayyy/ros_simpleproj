from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='p2',  
            executable='publisher',  
            name='publisher_node',
            output='screen',
        ),
        Node(
            package='p2',  
            executable='subscriber',  
            name='subscriber_node',
            output='screen',
        ),
    ])
