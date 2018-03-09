Changelog
=========

1.8 (unreleased)
----------------

- Require zest.releaser 4.0 as minimum, for ``execute_comand``.  [maurits]


1.7 (2016-07-13)
----------------

- Bugfixes for previous release:
  * Execute the checkout command
  * Correctly call super() in Git class
  * Fix header update in changelog
  [THijs]

- General improvements and corrections:
  * Update the main() functions to current zest.releaser equivalents
  * Update the __init__() functions to current zest.releaser equivalents
  * Use logger, not logging
  * Handle execute_comand complexity in one place
  * Reduce the amount of unnecessary modules
  * Some tidying and formatting
  [THijs]


1.6 (2016-06-29)
----------------

- 'feature/CMAAS-27':

  * Enhance original (OG) Git class instead of creating
    a new GitFlow
  * Have _push push to both develop and master branches
    from the gitflow settings
  * Check gitflow based on ./.git/config
  * Refactor choose to re-use as much of
    zest.releaser.choose as possible
  * Updated docstring formatting
  * Remove unused imports

  [THijs]

- 'feature/CMAAS-26':

  * Handle system() changing to execute_command()
  * Only supply the entry points that override
    zest.releaser, the rest gets built by it's
    respective packages.

  [THijs]


1.5 (2014-04-04)
----------------

- Nothing changed yet.


1.4 (2014-04-04)
----------------

- Nothing changed yet.


1.3 (2014-04-04)
----------------

- Nothing changed yet.


1.2 (2014-01-26)
----------------

- Nothing changed yet.


1.1 (2014-01-26)
----------------

- Initial release
