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

    def execute(self):
        """Make the changes and offer a commit"""
        self._write_version()
        if utils.gitflow_check(self.vcs):
            self._gitflow_release_start()
        self._write_history()
        self._diff_and_commit()

    def _gitflow_release_start(self):
        logging.info('Location: ' + utils.system('pwd'))
        cmd = self.vcs.cmd_gitflow_release_start(self.data['new_version'])
        print cmd
        if utils.ask("Run this command"):
            print system(cmd)

def main():
    utils.parse_options()
    logging.basicConfig(level=utils.loglevel(),
                        format="%(levelname)s: %(message)s")
    prereleaser = Prereleaser()
    prereleaser.run()
