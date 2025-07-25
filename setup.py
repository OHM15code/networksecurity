from setuptools import setup,find_packages
from typing import List
requirements_list=[]
def get_requirements()->  List[str]:
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirements=line.strip()
                if  requirements and requirements !="-e .":
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print("File not Found")

    return requirements_list
print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ohm Gupta",
    author_email="ohmgupta15@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
