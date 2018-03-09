# -*- coding: utf-8 -*-
""" Do the checks and tasks that have to happen before doing a release.
"""
from __future__ import unicode_literals
from egg.releaser.utils import has_extension
from egg.releaser.utils import prepare_vcs
from zest.releaser import prerelease
from zest.releaser import utils

import logging


logger = logging.getLogger(__name__)


class Prereleaser(prerelease.Prereleaser):
    """ Prepare release, ready for making a tag and an sdist.

        self.data holds data that can optionally be changed by plugins.
    """

    def __init__(self, vcs=None):
        vcs = prepare_vcs(vcs)
        super(Prereleaser, self).__init__(vcs=vcs)

    def _gitflow_release_start(self):
        logger.info('Location: ' + utils.execute_command(['pwd']))
        self.vcs.gitflow_check_branch('develop', switch=True)
        cmd = self.vcs.cmd_gitflow_release_start(self.data['new_version'])
        print(cmd)
        if utils.ask('Run this command'):
            print(utils.execute_command(cmd))

    def execute(self):
        """ Make the changes and offer a commit.
        """
        if has_extension(self.vcs, 'gitflow'):
            self._gitflow_release_start()
        super(Prereleaser, self).execute()


def main():
    utils.parse_options()
    utils.configure_logging()
    prereleaser = Prereleaser()
    prereleaser.run()
