from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flitton_fib.py",
    version="0.0.1",
    author="Robin Mumm",
    author_email="robinmumm@hotmail.com",
    description="Calculates a Fibonacci number",
    long_description=long_description,
    url="https://github.com/little-did-I-know/flitton-fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    test_require=['pytest']
)