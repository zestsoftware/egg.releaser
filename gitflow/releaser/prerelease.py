"""Do the checks and tasks that have to happen before doing a release.
"""

import logging

from zest.releaser import prerelease

from gitflow.releaser import utils
from gitflow.releaser import choose
from gitflow.releaser.utils import system

logger = logging.getLogger(__name__)


class Prereleaser(prerelease.Prereleaser):
    """Prepare release, ready for making a tag and an sdist.

    self.data holds data that can optionally be changed by plugins.

    """

    def __init__(self):
        prerelease.Prereleaser.__init__(self)
        self.vcs = choose.version_control()

def main():
    utils.parse_options()
    logging.basicConfig(level=utils.loglevel(),
                        format="%(levelname)s: %(message)s")
    prereleaser = Prereleaser()
    prereleaser.run()
