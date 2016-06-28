"""Do the checks and tasks that have to happen after doing a release.
"""
import logging

from zest.releaser import postrelease

from egg.releaser import choose
from egg.releaser import utils

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
