import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyispyb",
    version="1.0.0",
    author="ISPyB collaboration",
    author_email="ispyb-dev@esrf.fr",
    description="ISPyB backend server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ispyb/py-ispyb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: LGPL3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
