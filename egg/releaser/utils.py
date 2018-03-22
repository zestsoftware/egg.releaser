# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from git import enhance_with_gitflow
from zest.releaser.choose import version_control

import logging


logger = logging.getLogger(__name__)


def has_extension(vcs, extension):
    if hasattr(vcs, 'extensions') and extension in vcs.extensions:
        return True
    return False


def prepare_vcs(vcs):
    """ Set vcs on self before running __init__, i.e.:

        >>> def __init__(self, vcs=None):
        >>>     vcs = utils.prepare_vcs(vcs)
        >>>     super().__init__()

        This will deal with the vcs being set on baserelease, while we want
        to set it our own way, recognising gitflow.
    """

    # baserelease sets vcs on __init__ if vcs == None
    if vcs is None:
        # In our preparation, we do the same check in order to have vcs
        # defined when calling the super().__init__()
        return enhance_with_gitflow(version_control())
    # If vcs was set already, we're golden and we can return the previously
    # set value.
    return vcs
