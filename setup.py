
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

setup(name='usf_pcr',
      version='0.0.1',
      description='Removes clusters of pixels based on labels image regions',
      packages=['usf_pcr'],
      install_requires=install_requires)
