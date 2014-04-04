import logging

from zest.releaser.git import Git

logger = logging.getLogger(__name__)


class GitFlow(Git):
    """ Add command proxy for GitFlow to already existing git commands. """
    extension = 'gitflow'

    def cmd_create_tag(self, version, base=''):
        msg = "Release-%s" % version
        _start_cmd = 'git flow release start %s %s' % (version, base)
        _finish_cmd = 'git flow release finish -m "%s" %s' % (msg, version)
        return '; '.join([_start_cmd, _finish_cmd])

    def cmd_gitflow_release_start(self, version, base=''):
        return 'git flow release start %s %s' % (version, base)

    def cmd_gitflow_release_finish(self, version):
        return 'git flow release finish -m "Release-%s" %s' % (version,
                                                               version)

    def cmd_gitflow_hotfix_start(self, version, basename=''):
        return "git flow hotfix start %s %s" % (version, basename)

    def cmd_gitflow_hotfix_finish(self, version):
        return "git flow hotfix finish %s" % version
