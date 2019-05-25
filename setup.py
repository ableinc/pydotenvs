import setuptools
from pyenv import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyenv",
    version=__version__,
    author="AbleInc - Jaylen Douglas",
    author_email="douglas.jaylen@gmail.com",
    description="Import environment variables from your .env file or run as command line tool; PyEnv Cli.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/abledigital/scramble",
    keywords=['environment variables', 'deployments', 'settings', 'env', 'pyenv',
              'configurations', 'python'],
    packages=['pyenv'],
    entry_points='''
        [console_scripts]
        pyenv=pyenv.cli:pyenv
    ''',
    install_requires=[
          'click>=7.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
