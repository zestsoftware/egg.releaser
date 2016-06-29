# Have all the zest releaser utils, plus additions and overrides
from zest.releaser.utils import *


def has_extension(vcs, extension):
    if hasattr(vcs, 'extensions') and extension in vcs.extensions:
        return True
    return False
