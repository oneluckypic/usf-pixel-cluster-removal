
from setuptools import setup, find_packages

install_requires = ['click',
                    'matplotlib',
                    'numpy',
                    'opencv-python',
                    'pandas',
                    'pillow',
                    'pytest',
                    'pyyaml',
                    'sklearn',
                    'tqdm']

setup(name='usf_mosquitos',
      version='0.0.1',
      description='Aides to mosquito habitat identification',
      packages=['usf_mosquitos'],
      install_requires=install_requires)
