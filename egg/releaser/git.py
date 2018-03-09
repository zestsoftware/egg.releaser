# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from zest.releaser import utils
from zest.releaser.git import Git as OGGit

import ConfigParser
import io
import logging
import sys


logger = logging.getLogger(__name__)


class Git(OGGit):
    """ Command proxy for Git enhanced with gitflow commands.
    """

    def cmd_gitflow_release_start(self, version, base=''):
        return ['git', 'flow', 'release', 'start', version, base]

    def cmd_gitflow_release_finish(self, version):
        return ['git', 'flow', 'release', 'finish', '-m',
                '"Release-{}" {}'.format(version, version)]

    def cmd_gitflow_hotfix_start(self, version, basename=''):
        return ['git', 'flow', 'hotfix', 'start', version, basename]

    def cmd_gitflow_hotfix_finish(self, version):
        return ['git', 'flow', 'hotfix', 'finish', version]

    def _config(self):
        """ Parse the git config into a ConfigParser object.
        """
        config = open('./.git/config', 'r').read().replace('\t', '')
        config = config.replace('\t', '')  # ConfigParser doesn't like tabs
        parser = ConfigParser.ConfigParser()
        parser.readfp(io.StringIO(config))
        return parser

    @property
    def extensions(self):
        config = self._config()
        return ['gitflow'] if 'gitflow "branch"' in config.sections() else []

    def cmd_create_tag(self, version, message, sign=False):
        if 'gitflow' not in self.extensions:
            return super(Git, self).cmd_create_tag(
                version, message, sign=sign)
        msg = 'Release-{}'.format(version)
        _start_cmd = 'git flow release start {} {}'.format(version, message)
        _finish_cmd = 'git flow release finish -m "{}" {}'.format(
            msg, version)
        return [_start_cmd, _finish_cmd]

    def gitflow_branches(self):
        config = self._config()
        return dict(config.items('gitflow "branch"'))

    def gitflow_get_branch(self, branch):
        branches = self.gitflow_branches()
        if branch in branches:
            return branches.get(branch)
        logger.critical(
            '"%s" is not a valid gitflow branch.' % branch)
        sys.exit(1)

    def gitflow_prefixes(self):
        config = self._config()
        return dict(config.items('gitflow "prefix"'))

    def gitflow_get_prefix(self, prefix):
        prefixes = self.gitflow_prefixes()
        if prefix in prefixes:
            return prefixes.get(prefix)
        logger.critical(
            '"%s" is not a valid gitflow prefix.' % prefix)
        sys.exit(1)

    def gitflow_check_prefix(self, prefix):
        prefix = self.gitflow_get_prefix(prefix)
        current = self.current_branch()
        return current.startswith(prefix)

    def gitflow_check_branch(self, branch, switch=False):
        branch = self.gitflow_get_branch(branch)
        current = self.current_branch()
        if current == branch:
            return
        if switch:
            self.gitflow_switch_to_branch(branch, silent=False)
        else:
            logger.critical(
                'You are not on the "%s" branch.' % branch)
            sys.exit(1)

    def gitflow_switch_to_branch(self, branch, silent=True):
        if not silent:
            logger.info(
                'You are not on the "%s" branch, switching now.' % branch)
        utils.execute_command(self.cmd_checkout_from_tag(branch, '.'))

    def current_branch(self):
        return utils.execute_command([
            'git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()


def enhance_with_gitflow(vcs):
    """ Return the vcs determined by the original function, unless we are
        dealing with git, in which case we return our gitflow enhanced Git().
    """
    return Git() if isinstance(vcs, OGGit) else vcs
