from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

base_packages = ["sentence-transformers>=0.3.8"]

setup(
    name="translation-quality-estimator",
    version="0.1.0",
    description="To estimate the quality of translation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/theRay07/Translation-Quality-Estimator",
    author="Rishav Ray",
    author_email="rishavray29@gmail.com",
    license="MIT",
    classifiers=[
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["tqe"],
    install_requires=base_packages,
    python_requires=">=3.6",
)
