from setuptools import setup
from setuptools import find_packages
import os
from glob import glob

package_name = 'p2'  # Change to your package name

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # Install the package.xml file to the share directory
        ('share/' + package_name, ['package.xml']),  # Explicitly install package.xml

        # If you have any launch files, you can include them here
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        
        # Optionally include any other resource files, configuration files, etc.
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'publisher = p2.publisher:main',  # Your publisher script
            'subscriber = p2.subscriber:main',  # Your subscriber script
        ],
    },
)
