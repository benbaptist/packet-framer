from setuptools import find_packages, setup, Command

with open("packetframer/__version__.py", "r") as f:
    exec(f.read())

setup(
    name="PacketFramer",
    version=__version__,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    license="MIT",
    long_description=open("README.md").read(),
    include_package_data=True
)
