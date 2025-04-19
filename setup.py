from setuptools import find_packages, setup

setup(
    name="QASystem with haystack",
    version="0.0.1",
    author="gaurav",
    author_email="gauravgarwal9011@gmail.com",
    packages=find_packages(),
    install_requires=["pinecone-haystack","haystack-ai", "fastapi","uvicorn","python-dotenv","pathlib"]
)