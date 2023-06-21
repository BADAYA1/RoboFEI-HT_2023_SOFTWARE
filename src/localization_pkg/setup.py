from setuptools import setup

package_name = 'localization_pkg'
Viewer = "localization_pkg/Viewer"

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robofei',
    maintainer_email='luanawt43@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'localization_node = localization_pkg.localization_node:main'
        ],
    },
)
