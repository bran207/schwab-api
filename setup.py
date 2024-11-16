from setuptools import setup, find_packages

setup(
    name="schwab",
    version="0.0.1",
    description="A Python Wrapper for Schwab's Individual Trading API",
    author="Brandon Compertore",
    author_email="Brandon@Compertore.com",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "authlib",
        "requests",
    ],  # external packages as dependencies
)
