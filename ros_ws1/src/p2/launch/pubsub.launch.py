from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

#TOPIC = "chatter";
#get directory of package

package_share_dir = get_package_share_directory('p2')
    
#path to yaml configuration file
    
config_file = os.path.join(package_share_dir, 'config', 'param.yaml')



def generate_launch_description():
    return LaunchDescription([
        Node(
            package='p2',  
            executable='publisher',  
            name='publisher_node',
            output='screen',
            #parameters=[{"topic":TOPIC}],
            parameters=[config_file]
        ),
        Node(
            package='p2',  
            executable='subscriber',  
            name='subscriber_node',
            output='screen',
            #parameters=[{"topic":TOPIC}],
            parameters=[config_file]
        ),
    ])
