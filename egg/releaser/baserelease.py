""" Provide a base for the three releasers.
"""

import logging

from egg.releaser import utils

try:
    from egg.releaser.utils import execute_command
except ImportError:
    # Old version?
    from egg.releaser.utils import system as execute_command

logger = logging.getLogger(__name__)


class BasereleaseMixin(object):
    """ Mixin to override the baserelease inherited functions.
    """

    def _push(self):
        """ Offer to push changes, if needed.
        """
        push_cmds = self.vcs.push_commands()
        if not push_cmds:
            return
        if utils.ask("OK to push commits to the server?"):
            if utils.has_extension(self.vcs, 'gitflow'):
                # Push both develop and master branches. First push master,
                # then develop, because that is the branch we want to end on.
                for branch in [
                        self.vcs.gitflow_get_branch("master"),
                        self.vcs.gitflow_get_branch("develop")]:
                    if branch != self.vcs.current_branch():
                        self.vcs.gitflow_switch_to_branch(branch)

                    for push_cmd in push_cmds:
                        output = execute_command(push_cmd)
                        logger.info(output)
            else:
                for push_cmd in push_cmds:
                    output = execute_command(push_cmd)
                    logger.info(output)
