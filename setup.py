import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="holistics_python_api",
    version="0.0.1",
    author="Phat Vo",
    author_email="phat.vo@holistics.io",
    description="Package to export report's data from Holistics.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/holistics/holistics-python",
    packages=setuptools.find_packages(),
    classifiers=(
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
	python_requires='>=3, <4',
)
