# Have all the zest releaser utils, plus additions and overrides
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


def has_extension(vcs, extension):
    if hasattr(vcs, 'extensions') and extension in vcs.extensions:
        return True
    return False


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
