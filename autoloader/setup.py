import os

from setuptools import find_packages, setup

BUILD_ID = os.environ.get("VERSION") or 0


requirements = [
    "dacite>=1.6.0",
    "pyspark>=3.0,<3.1",
    "pyyaml==5.4",
    "typing-extensions>=3.10.0.0",
    "databricks-cli==0.15.0",
    "types-requests==2.25.6",
    "pandas==1.3.5",
    "cryptography==36.0.1",
    "PyArrow==6.0.1",
]
setup_requirements = [
    "pytest-runner",
]

setup(
    name="autoloader",
    author="Thor Fundament",
    version=f"0.2.{BUILD_ID}",
    description="Configuration driven ingestion of data",
    packages=find_packages(),
    install_requires=requirements,
    setup_requires=setup_requirements,
    entry_points={"console_scripts": ["auto=autoloader.__main__:main"]},
)
