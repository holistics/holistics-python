import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="holistics",
    version="0.0a10",
    author="Phat Vo",
    author_email="phat.vo@holistics.io",
    description="Package to export report's data from holistics.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/holistics/holistics-python",
    packages=['holistics','tests'],
    classifiers=(
		'Programming Language :: Python :: 3',		
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
	install_requires=[
        "requests", "pandas",
    ],
	test_suite='nose.collector',
    tests_require=['nose'],
    python_requires='>= 3, < 4',
)
