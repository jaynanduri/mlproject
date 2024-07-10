import setuptools
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "mlproject"
AUTHOR_USER_NAME = "jaynanduri"
SRC_REPO = "customCNNClassifier"
AUTHOR_EMAIL = "nanduri.j@northeastern.edu"
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of packages that need to be installed for running this project.
    
    params:
        file_path: requirements file path
    returns:
        list of required packages
    """
    req = []
    with open(file_path) as file:
        req = file.readlines()
        req = [r.replace("\n", "") for r in req]
        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)
    return req

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package implementing a CNN classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements('requirements.txt'),
)