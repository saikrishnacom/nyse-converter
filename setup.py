from setuptools import setup

setup(
    name='nyseconverter',
    version='0.1',
    description='NYSE converter',
    url='https://github.com/saikrishnacom/nyse-converter',
    author='srinivas',
    author_email='srinivas@example.com',
    license='MIT',
    packages=['nyseconverter'],
    zip_safe=False,
    install_requires = [
        "dask[complete]"
    ],
    entry_points = {
        'console_scripts': ['nyseconverter=nyseconverter:main'],
    }
)