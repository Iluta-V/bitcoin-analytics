from setuptools import setup, find_packages

setup(
    name="bitcoin_analytics",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
    ],
)
