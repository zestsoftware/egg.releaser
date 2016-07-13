""" Do the checks and tasks that have to happen after doing a release.
"""
import utils

from zest.releaser import postrelease


class Postreleaser(utils.BasereleaseMixin, postrelease.Postreleaser):
    """ Post-release tasks like resetting version number.

        self.data holds data that can optionally be changed by plugins.
    """

    def __init__(self, vcs=None):
        vcs = utils.prepare_vcs(vcs)
        postrelease.Postreleaser.__init__(self, vcs=vcs)

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
    utils.configure_logging()
    postreleaser = Postreleaser()
    postreleaser.run()
