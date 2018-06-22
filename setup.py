import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="holistics_python_api",
    version="0.0.8",
    author="Phat Vo",
    author_email="phat.vo@holistics.io",
    description="Package to export report's data from Holistics.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/holistics/holistics-python",
    packages=['holistics_python_api'],
    classifiers=(
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 2',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
	install_requires=[
        "requests", "pandas",
    ],
    python_requires='>=2, <4',
)
