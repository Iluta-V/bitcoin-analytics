from setuptools import setup, find_packages

setup(
    name="bitcoin_analytics",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Analysis of Bitcoin network usage (2009-2017) from 492,000 blocks",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
