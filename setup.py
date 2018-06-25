import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="holistics_python",
    version="0.1.5",
    author="Phat Vo",
    author_email="phat.vo@holistics.io",
    description="Package to export report's data from holistics.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/holistics/holistics-python",
    packages=['holistics_python'],
    classifiers=(
		'Programming Language :: Python :: 3',		
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
	install_requires=[
        "requests", "pandas",
    ],
    python_requires='>=3, <4',
)
