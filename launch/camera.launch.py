import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # sudo apt install libraspberrypi-bin b4l-utils ros-foxy-v4l2-camera
    # sudo apt install ros-foxy-image-transport-plugins ros-foxy-rqt-image-view

    return LaunchDescription([

        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            namespace='camera',
            parameters=[{
                'image_size': [640,480],
                'time_per_frame': [1, 6],
                'camera_frame_id': 'camera_link_optical'
                }]
    )
    ])
