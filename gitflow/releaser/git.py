import logging

from zest.releaser import git

logger = logging.getLogger(__name__)


class GitFlow(git.Git):
    """ Add command proxy for GitFlow to already existing git commands. """
    extension = 'gitflow'

    def cmd_create_tag(self, version, type='release', base=''):
        msg = "Finish-release-%s" % (version,)
        _start_cmd = 'git flow %s start %s %s' % (type, version, base)
        _finish_cmd = 'git flow %s finish %s -m "%s"' % (type, version, msg)
        return '; '.join([_start_cmd, _finish_cmd])

    def cmd_gitflow_start(self, version, type='release', base=''):
        return "git flow %s start %s %s" % (type, version, base)

    def cmd_gitflow_hotfix_start(self, version, basename=''):
        return "git flow hotfix start %s %s" % (version, basename)

    def cmd_gitflow_hotfix_finish(self, version):
        return "git flow hotfix finish %s" % version

