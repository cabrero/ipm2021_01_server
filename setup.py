from setuptools import find_packages, setup

setup(
    name= 'p1-server',
    version= '1.0.0',
    scripts= ['p1-server.py'],
    packages= find_packages(),
    package_data= {'p1server': ['data/intervalos.csv']},
    zip_safe= False,
    install_requires= [
        'flask',
    ],
)
