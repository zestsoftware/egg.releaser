from egg.releaser.git import Git
from zest.releaser.choose import version_control as og_version_control
from zest.releaser.git import Git as OGGit


def version_control():
    """ Return an object that provides the version control interface based
        on the detected version control system.
    """
    vcs = og_version_control()
    return Git() if isinstance(vcs, OGGit) else vcs
