import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplelayout-Xiaohu-Zheng",
    version="0.0.1",
    author="Xiaohu Zheng",
    author_email="zhengboy320@163.com",
    description="A simple layout package",
    long_description="Generate temperature field data, which is then used to train the temperature field deep learning agent model.",
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/idrl-assignment/2-simplelayout-generator-Xiaohu-Zheng",
    packages=["src/simplelayout"],
    platforms="any",
    install_requires=["pytest", "numpy", "matplotlib", "scipy"],
    entry_points={"console_scripts": ["simplelayout=simplelayout.__main__:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
