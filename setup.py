import os

import setuptools

requirements = []

path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="neispy",
    version="4.0.0",
    license="MIT",
    author="Ryu ju heon",
    author_email="SaidBySolo@gmail.com",
    description="open-neis-api wrapping with aiohttp",
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SaidBySolo/neispy",
    package_data={"koreanbots": ["py.typed"]},
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        # 패키지에 대한 태그
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
