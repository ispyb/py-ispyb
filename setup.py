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
    license="LGPL-3.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
    python_requires='>=3.6',
)
