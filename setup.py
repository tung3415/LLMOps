from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MULTI_AI_AGENT",
    version="0.1",
    author="Tung",
    packages=find_packages(),
    install_requires = requirements,
)