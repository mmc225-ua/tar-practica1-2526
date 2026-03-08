#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, PushRosNamespace


def generate_launch_description():
    # Argumento por CLI (default 7)
    numero_arg = DeclareLaunchArgument(
        'numero',
        default_value='7',
        description='Valor para el campo numero del mensaje (por defecto 7)'
    )
    numero = LaunchConfiguration('numero')

    grupo = GroupAction([
        # Namespace del grupo
        PushRosNamespace('miGrupo'),

        # Publisher (remap para que el topic NO sea absoluto)
        Node(
            package='p2pkg',
            executable='nodopub_ejercicio2',
            name='nodopub_ejercicio2',
            parameters=[{'numero': numero}],
            # IMPORTANTE: remapeamos el topic absoluto -> relativo
            # para que con namespace quede /miGrupo/topic_ejercicio2
            remappings=[('/topic_ejercicio2', 'topic_ejercicio2')],
            output='screen'
        ),

        # Subscriber (mismo remap)
        Node(
            package='p2pkg',
            executable='nodosub_ejercicio2',
            name='nodosub_ejercicio2',
            remappings=[('/topic_ejercicio2', 'topic_ejercicio2')],
            output='screen'
        ),
    ])

    return LaunchDescription([
        numero_arg,
        grupo
    ])
