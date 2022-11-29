from setuptools import find_packages, setup

DESCRIPTION = "一個簡單、方便的Google Chat Webhook函式庫"

setup(
    name="chat.py",
    version="0.0.1",
    author="sus2790",
    author_email="amengpan6@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sus2790/chat.py",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    install_requires=["aiohttp"],
)
