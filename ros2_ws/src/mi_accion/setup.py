from setuptools import find_packages, setup

package_name = 'mi_accion'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='miguel-docker',
    maintainer_email='miguel-docker@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'server = mi_accion.fibonacci_action_server:main',
            'client = mi_accion.fibonacci_action_client:main',
            'ej_fib_server = mi_accion.ejercicios_fibServer:main',
            'ej_fib_client = mi_accion.ejercicios_fibClient:main',
        ],
    },
)
