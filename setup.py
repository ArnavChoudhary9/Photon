from setuptools import setup, find_packages

VERSION: str = "0.0.0.xxx0"
with open("VERSION", 'r') as f: VERSION = f.read()

setup(
    name="Photon",
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,  # Include non-code files
    package_data={
        "Photon": ["*"],  # Specify additional paths
    },
    install_requires=[],
    description="A  game engine written in Python",
    author="Arnav Choudhary",
    author_email="arnavhoudhary.6969@gmail.com",
    url="https://github.com/arnavchoudhary9/photon",  # Replace with your repo
)
