from setup.tools import find_packages,setup



from setuptools import setup, find_packages

setup(
    name="student_performance_ml_project",
    version="1.0",
    description="A machine learning project for analyzing student performance",
    author="Koushik",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
    ],
)
