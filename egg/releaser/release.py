from zest.releaser import release

import logging
import sys
from . import utils


logger = logging.getLogger(__name__)


class Releaser(release.Releaser):
    """ Release the project by tagging it and optionally uploading to pypi.
    """

    def __init__(self, vcs=None):
        vcs = utils.prepare_vcs(vcs)
        super(Releaser, self).__init__(vcs=vcs)

    def execute(self):
        """ Do the actual releasing.
        """
        logger.info('Location: ' + utils.execute_command('pwd'))
        if not utils.has_extension(self.vcs, 'gitflow'):
            super(Releaser, self).execute()
        if not self.vcs.gitflow_check_prefix('release'):
            logger.critical(
                'You are not on a release branch, first run a prerelease '
                'or gitflow release.')
            sys.exit(1)
        self._gitflow_release_finish()
        current = self.vcs.current_branch()
        logger.info(
            ('Switching from ' + current +
             ' to master branch for egg generation.'))
        self.vcs.gitflow_check_branch('master', switch=True)
        self._release()
        logger.info('Switching to back to ' + current + ' branch.')
        self.vcs.gitflow_switch_to_branch(current)

    def _gitflow_release_finish(self):
        if self.data['tag_already_exists']:
            return
        cmd = self.vcs.cmd_gitflow_release_finish(self.data['version'])
        print(cmd)
        if utils.ask('Run this command'):
            print(utils.execute_command(cmd))


def main():
    utils.parse_options()
    utils.configure_logging()
    releaser = Releaser()
    releaser.run()
    tagdir = releaser.data.get('tagdir')
    if tagdir:
        logger.info('Reminder: tag checkout is in %s', tagdir)
