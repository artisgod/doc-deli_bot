import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='hls_lfcd_lds_driver',
            executable='hlds_laser_publisher',
            name='lds_laser',
            output='screen',
            parameters=[{
                'port': '/dev/ttyUSB0',  # Replace this with the correct port of your LDS-01 sensor
                'frame_id': 'laser_frame',
            }],
            remappings=[
                ('/scan', '/lds_scan')
            ]
        )
    ])
