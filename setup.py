from setuptools import setup, find_packages
setup(
      name = 'myPackage',
      version = '0.1',
      packages = find_packages(exclude = [ 'tests *']),
      license = 'MIT',
      decription = 'example python package',
      long_description =open('READMe.md').read(),
      install_requires = ['numpy'],
      url='https;//github.com/<username>/<package-name>',
      author = 'Annah Masunga',
      author_email = '<your Email>'
)