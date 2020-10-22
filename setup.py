from setuptools import find_packages, setup

setup(
    name='sample_project',
    packages=find_packages(),
    version='0.1.0',
    description='Hands-on session on Github Actions',
    author='J. Offenberg',
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "pre-commit==2.7.1"
        ]
    }
)
