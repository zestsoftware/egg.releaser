"""Do the checks and tasks that have to happen after doing a release.
"""
import logging

from zest.releaser import postrelease

from gitflow.releaser import choose
from gitflow.releaser import utils
from gitflow.releaser.utils import system

logger = logging.getLogger(__name__)

class Postreleaser(postrelease.Postreleaser):
    """Post-release tasks like resetting version number.

    self.data holds data that can optionally be changed by plugins.

    """

    def __init__(self):
        postrelease.Postreleaser.__init__(self)
        self.vcs = choose.version_control()

def main():
    utils.parse_options()
    logging.basicConfig(level=utils.loglevel(),
                        format="%(levelname)s: %(message)s")
    postreleaser = Postreleaser()
    postreleaser.run()
