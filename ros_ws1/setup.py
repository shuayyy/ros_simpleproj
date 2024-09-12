from setuptools import setup

package_name = 'py_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'publisher = py_package.publisher:main',
            'subscriber = py_package.subscriber:main',
        ],
    },
)
