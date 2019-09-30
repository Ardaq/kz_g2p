import setuptools

with open('README.md', 'r', encoding='utf8') as fh:
    long_des = fh.read()

setuptools.setup(
    name="g2p-kz",
    version="0.0.1",
    author="Ardaq",
    author_email="ardager@163.com",
    description="Kazakh language grapheme to phoneme converter",
    long_description=long_des,
    long_description_content_type="text/markdown",
    url="https://github.com/Ardaq/kz_g2p",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
