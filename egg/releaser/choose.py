from egg.releaser.git import Git
from zest.releaser import choose
from zest.releaser.git import Git as OGGit


def version_control():
    """ Return an object that provides the version control interface based
        on the detected version control system.
    """
    vcs = choose.version_control()
    return Git() if isinstance(vcs, OGGit) else vcs
