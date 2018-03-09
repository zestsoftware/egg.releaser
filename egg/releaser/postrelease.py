""" Do the checks and tasks that have to happen after doing a release.
"""
from zest.releaser import postrelease
from . import utils

import logging


logger = logging.getLogger(__name__)


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
            self.vcs.gitflow_check_branch('develop', switch=True)
        super(Postreleaser, self).execute()

    def _push(self):
        """ Offer to push changes, if needed.
        """
        if not utils.has_extension(self.vcs, 'gitflow'):
            return super(Postreleaser, self)._push()
        push_cmds = self.vcs.push_commands()
        if not push_cmds:
            return
        default_anwer = self.pypiconfig.push_changes()
        if not utils.ask(
                "OK to push commits to the server?", default=default_anwer):
            return
        # Push both develop and master branches. First push master,
        # then develop, because that is the branch we want to end on.
        for branch in [
                self.vcs.gitflow_get_branch('master'),
                self.vcs.gitflow_get_branch('develop')]:
            if branch != self.vcs.current_branch():
                self.vcs.gitflow_switch_to_branch(branch)
            for push_cmd in push_cmds:
                output = utils.execute_command(push_cmd)
                logger.info(output)


def main():
    utils.parse_options()
    utils.configure_logging()
    postreleaser = Postreleaser()
    postreleaser.run()
