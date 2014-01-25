from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='gitflow.releaser',
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
      namespace_packages=['gitflow'],
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
              'release = gitflow.releaser.release:main',
              'prerelease = gitflow.releaser.prerelease:main',
              'postrelease = gitflow.releaser.postrelease:main',
              'fullrelease = gitflow.releaser.fullrelease:main',
              'longtest = gitflow.releaser.longtest:main',
              'lasttagdiff = gitflow.releaser.lasttagdiff:main',
              'lasttaglog = gitflow.releaser.lasttaglog:main',
              ],
          # The datachecks are implemented as entry points to be able to check
          # our entry point implementation.
          'gitflow.releaser.prereleaser.middle': [
              'datacheck = gitflow.releaser.prerelease:datacheck',
              ],
          'gitflow.releaser.releaser.middle': [
              'datacheck = gitflow.releaser.release:datacheck',
              ],
          'gitflow.releaser.postreleaser.middle': [
              'datacheck = gitflow.releaser.postrelease:datacheck',
              ],
          # Documentation generation
          'gitflow.releaser.prereleaser.before': [
              'datacheck = gitflow.releaser.utils:prepare_documentation_entrypoint',
              ],

          },
      )
