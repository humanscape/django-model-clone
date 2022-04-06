import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-model-clone", # Replace with your own username
    version="0.0.1",
    author="humanscape-june",
    author_email="june.333@humanscape.io",
    description="duplication of django model object",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/humanscape/django-model-clone",
    packages=setuptools.find_packages(),
    keywords=[
        "django",
        "django-clone",
        "django clone",
        "django object clone",
        "clone-django",
        "model cloning",
        "django instance duplication",
        "django duplication",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django :: 3.1",
    ],
    license="ISC",
    python_requires='>=3.6',
)