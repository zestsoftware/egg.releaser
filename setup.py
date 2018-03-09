from setuptools import find_packages
from setuptools import setup

import os


version = '1.8.dev0'

setup(name='egg.releaser',
      version=version,
      description="zest.releaser wrapper for use with git flow",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # https://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
      ],
      keywords='release git flow',
      author='Maurits van Rees',
      author_email='m.van.rees@zestsoftware.nl',
      url='https://github.com/zestsoftware/egg.releaser',
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
