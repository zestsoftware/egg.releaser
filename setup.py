from setuptools import setup, find_packages
import os

version = '1.5'

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
          'zest.releaser',
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              # zest.releaser scripts
              'longtest = zest.releaser.longtest:main',
              'lasttagdiff = zest.releaser.lasttagdiff:main',
              'lasttaglog = zest.releaser.lasttaglog:main',
              # egg.releaser scripts
              'prerelease = egg.releaser.prerelease:main',
              'release = egg.releaser.release:main',
              'postrelease = egg.releaser.postrelease:main',
              'fullrelease = egg.releaser.fullrelease:main',
              ],
          # The datachecks are implemented as entry points to be able to check
          # our entry point implementation.
          'zest.releaser.prereleaser.middle': [
              'datacheck = zest.releaser.prerelease:datacheck',
              ],
          'zest.releaser.releaser.middle': [
              'datacheck = zest.releaser.release:datacheck',
              ],
          'zest.releaser.postreleaser.middle': [
              'datacheck = zest.releaser.postrelease:datacheck',
              ],
          # Documentation generation
          'zest.releaser.prereleaser.before': [
              'datacheck = '
                  'zest.releaser.utils:prepare_documentation_entrypoint',
              ],

          },
      )
