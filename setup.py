from setuptools import setup, find_packages

setup(
    name='pygiga',
    version='0.1.0',
    description='PyGiga AI agent framework',
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.0',
        'grpcio>=1.56.0',
    ],
    python_requires='>=3.8',
    include_package_data=True,
)
