import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="hailtheking-reader-realpython",
    version="1.0.0",
    description="A easy and quick way to get help from realpythons latest articles onto your terminal",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/HailtheKing2024/Python/tree/main/pythonreader",
    author="Abhinav B",
    author_email="bijishabhinav@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)