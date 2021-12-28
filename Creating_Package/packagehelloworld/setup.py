from setuptools import setup, find_packages

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(name="packagehelloworld",
      version="0.0.1",
      description="This is a Hellow World Package",
      long_description="This is a dummy description field",
      author="Jaidip",
      author_email="jaidip1994@gmai.com",
      # Will be returing, the packages (['packagehelloworld'])
      packages=find_packages(),
      install_requires=REQUIREMENTS
      )
