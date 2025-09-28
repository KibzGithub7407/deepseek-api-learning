from setuptools import setup, find_packages

setup(
    name="deepseek-api-learning",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "python-dotenv>=0.19.0",
    ],
)
