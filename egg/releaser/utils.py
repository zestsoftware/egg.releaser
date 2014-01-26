from zest.releaser.utils import *

def gitflow_check(vcs):
    if hasattr(vcs, 'extension') and vcs.extension == 'gitflow':
        return True
    return False