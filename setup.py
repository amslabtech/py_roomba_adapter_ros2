from setuptools import find_packages
from setuptools import setup

package_name = 'py_roomba_adapter_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_dir={package_name: package_name},
    package_data={package_name: ['config/*']},
    data_files=[],
    install_requires=['setuptools'],
    zip_safe=True,
    author='amsl',
    author_email='',
    maintainer='',
    maintainer_email='',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
    ),
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_detector = py_roomba_adapter_ros2.object_detector:main'
        ],
    },
)
