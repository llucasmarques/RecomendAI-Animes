from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="RECOMMENDAI-Animes",
    version="0.1",
    author="Lucas",
    packages=find_packages(),
    install_requires = requirements,
)