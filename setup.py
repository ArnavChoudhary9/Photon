from setuptools import setup, find_packages

VERSION: str = "0.0.0.xxx0"
with open("Photon/Core/VERSION", 'r') as f: VERSION = f.read()

long_description = ""
with open("README.md") as f:
    long_description = f.read()

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

requirements = parse_requirements('requirements.txt')

setup(
    name="PhotonEngine",
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,  # Include non-code files
    package_data={
        "Photon": ["*"],  # Specify additional paths
        "Photon.Core": ["VERSION"],
    },
    install_requires=requirements,
    description="A  game engine written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Arnav Choudhary",
    author_email="arnavhoudhary.6969@gmail.com",
    url="https://github.com/arnavchoudhary9/photon",  # Replace with your repo,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11"
    ],
)
