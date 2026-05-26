from setuptools import setup
from glob import glob
import os

package_name = 'turtle_patrol'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            os.path.join('share', package_name, 'action'),
            glob('action/*.action')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tara',
    maintainer_email='tara@todo.todo',
    description='Turtle Patrol Action Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'circle_patrol_server = turtle_patrol.circle_patrol_server:main',
            'circle_patrol_client = turtle_patrol.circle_patrol_client:main',
        ],
    },
)

