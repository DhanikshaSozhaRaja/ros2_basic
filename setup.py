from setuptools import setup

package_name = 'robot_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
        (
            'share/' + package_name + '/launch',
            [
                'launch/display.launch.py',
                'launch/gazebo.launch.py',
            ],
        ),
        (
            'share/' + package_name + '/urdf',
            [
                'urdf/robot.urdf.xacro',
            ],
        ),
        (
            'share/' + package_name + '/worlds',
            [
                'worlds/custom_world.sdf',
            ],
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dhaniksha',
    maintainer_email='dhaniksha@example.com',
    description='Robot simulation package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
