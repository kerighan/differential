from setuptools import setup


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


reqs = parse_requirements("requirements.txt")


setup(
    name="differential",
    version="1.0.0",
    author="Maixent Chenebaux",
    author_email="max.chbx@gmail.com",
    description="differential equations with cool syntax",
    long_description_content_type="text/markdown",
    install_requires=reqs,
    packages=["differential"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
