import logging

from zest.releaser import release
from egg.releaser import choose
from egg.releaser import utils
from egg.releaser.utils import system


class Releaser(release.Releaser):
    """Release the project by tagging it and optionally uploading to pypi."""

    def __init__(self):
        release.Releaser.__init__(self)
        self.vcs = choose.version_control()

    def execute(self):
        """Do the actual releasing"""
        logging.info('Location: ' + utils.system('pwd'))
        if utils.gitflow_check(self.vcs):
            self._gitflow_release_finish()
        else:
            self._make_tag()
        self._release()

    def _gitflow_release_finish(self):
        if self.data['tag_already_exists']:
            return
        cmd = self.vcs.cmd_gitflow_release_finish(self.data['version'])
        print cmd
        if utils.ask("Run this command"):
            print system(cmd)

def main(return_tagdir=False):
    utils.parse_options()
    logging.basicConfig(level=utils.loglevel(),
                        format="%(levelname)s: %(message)s")
    releaser = Releaser()
    releaser.run()
    if return_tagdir:
        # At the end, for the benefit of fullrelease.
        return releaser.data.get('tagdir')
    else:
        tagdir = releaser.data.get('tagdir')
        if tagdir:
            logging.info("Reminder: tag checkout is in %s", tagdir)
