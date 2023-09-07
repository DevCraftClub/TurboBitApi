from setuptools import setup

setup(
    name="turbobit_api",
    version="1.0.0",
    description="Unofficial python api wrapper from https://turbobit.net/",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords="api turbobit file video hosting unlimited",
    url="https://github.com/DevCraftClub/TurboBitApi",
    author="Maxim Harder",
    author_email="dev@devcraft.club",
    packages=["turbobit_api"],
    install_requires=[
        "requests",
        "python-dotenv",
        "python-fsutil"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
