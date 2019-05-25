import setuptools
from pyenv import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyenv",
    version=__version__,
    author="AbleInc - Jaylen Douglas",
    author_email="douglas.jaylen@gmail.com",
    description="Import your environment variables, manually or automted.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/abledigital/scramble",
    keywords=['environment variables', 'deployments', 'settings', 'env', 'dotenv',
              'configurations', 'python'],
    packages=setuptools.find_packages(),
    entry_points='''
        [console_scripts]
        pyenv=pyenv.cli:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
