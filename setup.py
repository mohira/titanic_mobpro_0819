from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ""

try:
    with open('LICENSE') as f:
        license = f.read()
except IOError:
    license = ""

try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except IOError:
    requirements = []

setup(
    name='titanic_src',
    version='0.0.0',
    packages=find_packages(exclude=("tests", "docs")),
    url='https://github.com/mohira/titanic_mobpro_0819.git',
    license=license,
    author='sarrrrry',
    author_email='sarrrrry.sarrrrry@gmail.com',
    description='',
    long_description=readme,
    python_requires="==3.6.5",
    install_requires=[
        *requirements,
    ]
)
