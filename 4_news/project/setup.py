from setuptools import setup, find_packages

setup(
    name='nytimes-crawler',
    version='1.0',
    author='Bernardas Ališauskas',
    description='articles crawler for nytimes.com',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'aiohttp',
        'parsel',
    ],
    entry_points={
        'console_scripts': [
            f'nytimes=nytimes.cli:main'
        ],
    },
)
