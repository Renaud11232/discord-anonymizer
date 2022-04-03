import setuptools


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


setuptools.setup(
    name="discordanonymizer",
    version="0.1.0rc1",
    author="Renaud Gaspard",
    author_email="gaspardrenaud@hotmail.com",
    description="A simple bot that anonymously reposts received PM on a guild channel",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Renaud11232/discord-anonymizer",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "discordanonymizer=discordanonymizer.command_line:main"
        ]
    },
    install_requires=[
        "nextcord"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)