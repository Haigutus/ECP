from setuptools import setup
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ecp-api',
    version=versioneer.get_version().split("+")[0],
    cmdclass=versioneer.get_cmdclass(),
    packages=['ECP'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Haigutus/ECP',
    license='GPL2',
    author='Kristjan Vilgo',
    author_email='kristjan.vilgo@gmail.com',
    description='ENTSO-E ECP software MADES SOAP API implementation in python',
    install_requires=[
        "requests", "zeep", 'urllib3', "lxml"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ]
)
