""" Do the checks and tasks that have to happen before doing a release.
"""

import logging
import utils

from zest.releaser import prerelease

logger = logging.getLogger(__name__)


class Prereleaser(prerelease.Prereleaser):
    """ Prepare release, ready for making a tag and an sdist.

        self.data holds data that can optionally be changed by plugins.
    """

    def __init__(self, vcs=None):
        vcs = utils.prepare_vcs(vcs)
        prerelease.Prereleaser.__init__(self, vcs=vcs)

    def _gitflow_release_start(self):
        logger.info('Location: ' + utils.execute_command('pwd'))
        self.vcs.gitflow_check_branch("develop", switch=True)
        cmd = self.vcs.cmd_gitflow_release_start(self.data['new_version'])
        print cmd
        if utils.ask("Run this command"):
            print utils.execute_command(cmd)

    def execute(self):
        """ Make the changes and offer a commit.
        """
        if utils.has_extension(self.vcs, 'gitflow'):
            self._gitflow_release_start()
        self._change_header()
        self._write_version()
        self._write_history()
        self._diff_and_commit()


def main():
    utils.parse_options()
    utils.configure_logging()
    prereleaser = Prereleaser()
    prereleaser.run()
