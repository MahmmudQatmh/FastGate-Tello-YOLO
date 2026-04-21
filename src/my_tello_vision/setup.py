from setuptools import setup
import os
from glob import glob

package_name = 'my_tello_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Includes launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # IMPORTANT: This copies your YOLO models into the install directory
        (os.path.join('share', package_name, 'models'), glob('models/*.pt')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mahmmudqatmh',
    maintainer_email='pro4mahmoudqatmh@gmail.com',
    description='Autonomous DJI Tello control using YOLO and ROS 2 Humble',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tello_vision_control = my_tello_vision.tello_vision_control:main',
            'calibrate = my_tello_vision.calibrate:main',
            'record_tello = my_tello_vision.record_tello:main',
            'record_tello_raw = my_tello_vision.record_tello_raw:main'
        ],
    },
)
