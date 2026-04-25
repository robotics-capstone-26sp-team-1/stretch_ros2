import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    dict_file_path = os.path.join(get_package_share_directory('stretch_core'), 'config', 'stretch_marker_dict.yaml')
    depth_topic_name_arg = DeclareLaunchArgument(
        'depth_topic_name',
        default_value='/camera/depth/image_rect_raw',
        description='Depth image topic used by the ArUco detector',
    )

    detect_aruco_markers = Node(
        package='stretch_core',
        executable='detect_aruco_markers',
        output='screen',
        parameters=[dict_file_path],
        remappings=[
            ('/camera/aligned_depth_to_color/image_raw', LaunchConfiguration('depth_topic_name')),
        ],
        )

    return LaunchDescription([
        depth_topic_name_arg,
        detect_aruco_markers,
        ])
