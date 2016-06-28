""" Do the checks and tasks that have to happen before doing a release.
"""

import logging

from zest.releaser import prerelease

from egg.releaser import utils
from egg.releaser import choose

try:
    from egg.releaser.utils import execute_command
except ImportError:
    # Old version?
    from egg.releaser.utils import system as execute_command

logger = logging.getLogger(__name__)


class Prereleaser(prerelease.Prereleaser):
    """ Prepare release, ready for making a tag and an sdist.

        self.data holds data that can optionally be changed by plugins.
    """

    def __init__(self):
        prerelease.Prereleaser.__init__(self)
        self.vcs = choose.version_control()

    def execute(self):
        """Make the changes and offer a commit"""
        if utils.gitflow_check(self.vcs):
            self._gitflow_release_start()
        self._write_version()
        self._write_history()
        self._diff_and_commit()

    def _gitflow_release_start(self):
        logging.info('Location: ' + execute_command('pwd'))
        cmd = self.vcs.cmd_gitflow_release_start(self.data['new_version'])
        print cmd
        if utils.ask("Run this command"):
            print execute_command(cmd)

def main():
    utils.parse_options()
    logging.basicConfig(level=utils.loglevel(),
                        format="%(levelname)s: %(message)s")
    prereleaser = Prereleaser()
    prereleaser.run()
