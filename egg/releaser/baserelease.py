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
        """Offer to push changes, if needed."""
        push_cmds = self.vcs.push_commands()
        if not push_cmds:
            return
        print "Right file"
        if utils.ask("OK to push commits to the server?"):
            if utils.has_extension(self.vcs, 'gitflow'):
                original_branch = self.vcs.current_branch()

                # Push both develop and master branches
                for branch in self.vcs.gitflow_branches():
                    # Switch branch when necessary
                    if branch != original_branch:
                        self.vcs.cmd_checkout_from_tag(branch, '.')
                    for push_cmd in push_cmds:
                        output = execute_command(push_cmd)
                        logger.info(output)

                # Switch back to original_branch
                if branch != original_branch:
                    self.vcs.cmd_checkout_from_tag(original_branch, '.')
            else:
                for push_cmd in push_cmds:
                    output = execute_command(push_cmd)
                    logger.info(output)
