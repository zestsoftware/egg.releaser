import logging
import tempfile
import os
import os.path
import sys

from zest.releaser.utils import system
from zest.releaser.git import Git

logger = logging.getLogger(__name__)

class GitFlow(Git):
    """Command proxy for GitFlow"""

    def cmd_flow_release_start(self, version, base=''):
        return "git flow release start %s %s" % (version, base)

    def cmd_flow_release_publish(self, version):
        return "git flow release publish %s" % version

    def cmd_flow_release_finish(self, version):
        return "git flow release finish %s" % version

    def cmd_flow_hotfix_start(self, version, basename=''):
        return "git flow hotfix start %s %s" % (version, basename)

    def cmd_flow_hotfix_finish(self, version):
        return "git flow hotfix finish %s" % version

