import logging

# Have all the zest releaser utils, plus additions and overrides
from git import enhance_with_gitflow

from zest.releaser.choose import version_control
try:
    # Older zest.releaser.utils have system to fulfill the execute_command
    # function. First try importing this.
    from zest.releaser.utils import system as execute_command
except ImportError:
    # No more system, we are dealing with a newer version
    pass
# Now import everything. If execute_command is present in utils, it will
# override the previous 'import as'.
from zest.releaser.utils import *

logger = logging.getLogger(__name__)


def has_extension(vcs, extension):
    if hasattr(vcs, 'extensions') and extension in vcs.extensions:
        return True
    return False


def prepare_vcs(vcs):
    """ Set vcs on self before running __init__, i.e.:

        >>> def __init__(self, vcs=None):
        >>>     vcs = utils.prepare_vcs(vcs)
        >>>     super().__init__()

        This will deal with the vcs being set on baserelease, while we want
        to set it our own way, recognising gitflow.
    """

    # baserelease sets vcs on __init__ if vcs == None
    if vcs is None:
        # In our preparation, we do the same check in order to have vcs
        # defined when calling the super().__init__()
        return enhance_with_gitflow(version_control())
    # If vcs was set already, we're golden and we can return the previously
    # set value.
    return vcs


class BasereleaseMixin(object):
    """ Mixin to override the baserelease inherited functions.
    """

    def _push(self):
        """ Offer to push changes, if needed.
        """
        push_cmds = self.vcs.push_commands()
        if not push_cmds:
            return
        if ask("OK to push commits to the server?"):
            if has_extension(self.vcs, 'gitflow'):
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
