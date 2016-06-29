""" Do the prerelease, actual release and post release in one fell swoop!
"""
import logging
import os


from egg.releaser import prerelease
from egg.releaser import release
from egg.releaser import postrelease
from egg.releaser import utils

logger = logging.getLogger(__name__)


def main():
    utils.parse_options()
    logging.basicConfig(level=utils.loglevel(),
                        format="%(levelname)s: %(message)s")
    logger.info('Starting prerelease.')
    original_dir = os.getcwd()
    prerelease.main()
    os.chdir(original_dir)
    logger.info('Starting release.')
    tagdir = release.main(return_tagdir=True)
    os.chdir(original_dir)
    logger.info('Starting postrelease.')
    postrelease.main()
    os.chdir(original_dir)
    logger.info('Finished full release.')
    if tagdir:
        logger.info("Reminder: tag checkout is in %s", tagdir)
