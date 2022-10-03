import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "Deep_CNN_Classifier"
AUTHOR_USERNAME = "astajyoti1"
SRC_REPO = "DeepClassifier"
AUTHOR_EMAIL = "astajyoti@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USERNAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for CNN App",
    long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"
        },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)
