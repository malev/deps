from setuptools import setup, find_packages

setup(
    name='deps',
    version='0.1.0',
    author='Marcos Vanetta',
    author_email='marcosvanetta@gmail.com',
    url='http://github.com/malev/deps',
    description='Environment.yml parser',
    packages=find_packages(),
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'deps = deps.cli:main',
        ]
    }
)
