from setuptools import setup, find_packages

setup(
    name='football-monitor',
    version='1.0',
    author='Bernardas Ališauskas',
    description='Crawler and monitor for football matches',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'parsel'
    ],
    entry_points={
        'console_scripts': [
            f'football=football.cli:main'
        ],
    },
)
