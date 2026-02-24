from setuptools import setup, find_packages

setup(
    name="nodezerov2",
    version="0.1.0",
    packages=find_packages(include=["nodezero_v2*"]),
    install_requires=[
        "numpy",
        "pytest>=7.0"
    ],
    tests_require=["pytest"],
    author="Luke Vinehout",
    description="AI Safety Gates: Drift/Tox blocks"
)
