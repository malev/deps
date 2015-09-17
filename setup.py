from setuptools import setup, find_packages
import versioneer

setup(
    name='ibu',
    version='0.0.1',
    author='Marcos Vanetta',
    author_email='marcosvanetta@gmail.com',
    url='http://github.com/malev/ibu',
    description='Dependencies parser',
    packages=find_packages(),
    scripts=[
        'bin/ibu',
    ]
)
