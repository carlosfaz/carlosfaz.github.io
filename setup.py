import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

import versioneer

setuptools.setup(
    name="FM1",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Carlos Faz",
    author_email="cefj94@gmail.com",
    description="Some files",
    long_description=long_description,
    url="https://github.com/carlosfaz/FM1/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires= '>=3.6',
    install_requires=[
        'sphinx'
    ],
    license='MIT',
)
