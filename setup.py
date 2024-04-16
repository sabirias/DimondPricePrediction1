from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name="DimondPricePrediction",
    version='0.0.1',
    author='Mohammed Sabir',
    author_email='saabirrazviias@gmail.com',
    install_requires=get_requirements('requirements.txt'),  # Updated file path to requirements.txt
    packages=find_packages()
)
