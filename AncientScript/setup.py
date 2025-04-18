from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="ancient-scripts",
    version="1.0.0",
    description="Conversion tool for ancient writing systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ancient-scripts",
    author="Your Name",
    author_email=" amirhossinpython03@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords="ancient, scripts, cuneiform, hieroglyph, linguistics",
    package_dir={"": "ancient_scripts"},
    packages=find_packages(where="ancient_scripts"),
    python_requires=">=3.8, <4",
    install_requires=[
        "deep-translator>=1.11.0",
        "numpy>=1.21.0",
    ],
    package_data={
        "ancient_scripts": ["data/*.json"],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ancient-scripts/issues",
        "Source": "https://github.com/yourusername/ancient-scripts",
    },
)