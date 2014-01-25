import pkg_resources

from zest.releaser import fullrelease
from zest.releaser import lasttagdiff
from zest.releaser import lasttaglog
from zest.releaser import longtest
from zest.releaser import postrelease
from zest.releaser import prerelease
from zest.releaser import release

__version__ = pkg_resources.get_distribution("gitflow.releaser").version
