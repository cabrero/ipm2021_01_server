from setuptools import find_packages, setup

setup(
    name='p1-server',
    version='1.0.0',
    scripts=['p1server/p1-server.py'],
    packages=find_packages(),
    include_package_data=True,
    data_files = [('data', ['p1server/intervalos.csv'])],
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
