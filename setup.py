
from distutils.core import setup

setup(
    name='NeuralynxIO',
    version='0.2',
    description='Neuralynx file parser',
    author='Ryan',
    author_email='yarnnd@gmail.com',
    url='https://github.com/Yarn/NeuralynxIO',
    packages=['neuralynx_io'],
    install_requires=[
        'numpy>=1.23.3',
    ],
)
