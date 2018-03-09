from setuptools import find_packages
from setuptools import setup

import os


version = '1.8.dev0'

setup(name='egg.releaser',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['egg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zest.releaser >= 4.0',
      ],
      entry_points={
          'console_scripts': [
              # egg.releaser scripts
              'prerelease = egg.releaser.prerelease:main',
              'release = egg.releaser.release:main',
              'postrelease = egg.releaser.postrelease:main',
              'fullrelease = egg.releaser.fullrelease:main',
          ],

      },
      )
