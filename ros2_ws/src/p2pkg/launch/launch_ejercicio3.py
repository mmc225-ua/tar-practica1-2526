#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Argumento por línea de comandos (default 7)
    numero_arg = DeclareLaunchArgument(
        'numero',
        default_value='7',
        description='Valor para el campo numero del mensaje (por defecto 7)'
    )

    numero = LaunchConfiguration('numero')

    pub_node = Node(
        package='p2pkg',
        executable='nodopub_ejercicio2',
        name='nodopub_ejercicio2',
        parameters=[{'numero': numero}],
        output='screen'
    )

    sub_node = Node(
        package='p2pkg',
        executable='nodosub_ejercicio2',
        name='nodosub_ejercicio2',
        output='screen'
    )

    return LaunchDescription([
        numero_arg,
        pub_node,
        sub_node
    ])
