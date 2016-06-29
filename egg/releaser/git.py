import logging
import ConfigParser
import io

from zest.releaser.git import Git as OGGit

try:
    from egg.releaser.utils import execute_command
except ImportError:
    # Old version?
    from egg.releaser.utils import system as execute_command

logger = logging.getLogger(__name__)


class Git(OGGit):
    """ Command proxy for Git enhanced with gitflow commands.
    """

    def cmd_gitflow_release_start(self, version, base=''):
        return 'git flow release start %s %s' % (version, base)

    def cmd_gitflow_release_finish(self, version):
        return 'git flow release finish -m "Release-%s" %s' % (version,
                                                               version)

    def cmd_gitflow_hotfix_start(self, version, basename=''):
        return "git flow hotfix start %s %s" % (version, basename)

    def cmd_gitflow_hotfix_finish(self, version):
        return "git flow hotfix finish %s" % version

    def _config():
        """ Parse the git config into a ConfigParser object.
        """
        config = open('./.git/config', 'r').read().replace('\t', '')
        config = config.replace('\t', '')  # ConfigParser doesn't like tabs
        parser = ConfigParser.ConfigParser()
        parser.readfp(io.BytesIO(config))
        return parser

    @property
    def extensions(self):
        config = self._config()
        return ['gitflow'] if 'gitflow "branch"' in config.sections() else []

    def cmd_create_tag(self, version, base=''):
        if 'gitflow' in self.extensions:
            msg = "Release-%s" % version
            _start_cmd = 'git flow release start %s %s' % (version, base)
            _finish_cmd = 'git flow release finish -m "%s" %s' % (msg, version)
            return '; '.join([_start_cmd, _finish_cmd])
        else:
            super(OGGit, self).cmd_create_tag(self, version)

    def gitflow_branches(self):
        config = self._config()
        return [
            config.get('gitflow "branch"', branch)
            for branch in ['develop', 'master']]

    def current_branch(self):
        return execute_command("git rev-parse --abbrev-ref HEAD").strip()
