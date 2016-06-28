import logging
import os
import sys
from egg.releaser import git
from zest.releaser import hg
from zest.releaser import bzr
from zest.releaser import svn
from zest.releaser import choose

try:
    from egg.releaser.utils import system as execute_command
except ImportError:
    from egg.releaser.utils import execute_command

logger = logging.getLogger(__name__)


def version_control():
    """Return an object that provides the version control interface based
    on the detected version control system."""
    curdir_contents = os.listdir('.')
    # prefer git over all and everything over svn
    if '.git' in curdir_contents:
        config = open('./.git/config', 'r').read()
        if config.find('gitflow') > -1:
            return git.GitFlow()
        return git.Git()
    elif '.hg' in curdir_contents:
        return hg.Hg()
    elif '.bzr' in curdir_contents:
        return bzr.Bzr()
    elif '.svn' in curdir_contents:
        return svn.Subversion()
    else:
        # Try finding an svn checkout *not* in the root.
        last_try = execute_command("svn info")
        if 'Repository' in last_try:
            return svn.Subversion()
        logger.critical('No version control system detected.')
        sys.exit(1)

