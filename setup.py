import setuptools

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="neispy",
    version="3.2.1",
    license="MIT",
    author="Ryu ju heon",
    author_email="SaidBySolo@gmail.com",
    description="open-neis-api wrapping with aiohttp",
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SaidBySolo/neispy",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
