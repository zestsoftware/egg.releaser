import logging

from zest.releaser import release
from gitflow.releaser import choose
from gitflow.releaser import utils


class Releaser(release.Releaser):
    """Release the project by tagging it and optionally uploading to pypi."""

    def __init__(self):
        release.Releaser.__init__(self)
        self.vcs = choose.version_control()

    def execute(self):
        """Do the actual releasing"""
        import pdb; pdb.set_trace()

        self.vcs = choose.version_control()
        self._make_tag()
        self._release()

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
            logger.info("Reminder: tag checkout is in %s", tagdir)
