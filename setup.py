from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str)->List[str]:
    '''
    Essa funcao retornara uma lista do arquivo requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
        

setup(
    name='mlproject',
    version='0.0.1',
    author='Matheus',
    author_email = 'matcgoes@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')   
)