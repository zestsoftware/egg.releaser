""" Do the checks and tasks that have to happen after doing a release.
"""
import logging

from zest.releaser import postrelease

from egg.releaser import choose
from egg.releaser import utils
from egg.releaser.baserelease import BasereleaseMixin

logger = logging.getLogger(__name__)


class Postreleaser(BasereleaseMixin, postrelease.Postreleaser):
    """ Post-release tasks like resetting version number.

        self.data holds data that can optionally be changed by plugins.
    """

    def __init__(self):
        postrelease.Postreleaser.__init__(self)
        self.vcs = choose.version_control()

    def execute(self):
        """ Make the changes and offer a commit.
        """
        if utils.has_extension(self.vcs, 'gitflow'):
            self.vcs.gitflow_check_branch("develop", switch=True)
        self._write_version()
        self._change_header(add=True)
        self._write_history()
        self._diff_and_commit()
        self._push()


def main():
    utils.parse_options()
    logging.basicConfig(level=utils.loglevel(),
                        format="%(levelname)s: %(message)s")
    postreleaser = Postreleaser()
    postreleaser.run()
