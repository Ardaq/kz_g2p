import setuptools
import os

dirname = os.path.dirname(__file__)

with open('README.md', 'r', encoding='utf8') as fh:
    long_des = fh.read()

setuptools.setup(
    name="g2p-kz",
    version="0.0.3",
    author="Ardaq",
    author_email="ardager@163.com",
    description="Kazakh language grapheme to phoneme converter",
    long_description=long_des,
    long_description_content_type="text/markdown",
    url="https://github.com/Ardaq/kz_g2p",
    packages=setuptools.find_packages(),
    package_data={'kzphoneme': ['data/*.*']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    keywords=[
        "Kazakh",
        "Phoneme",
    ],
    python_requires='>=3.6',
    install_requires=[
        "nltk >= 3.4.5",
    ],
)
