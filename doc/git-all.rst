``git all``: Perform a command on each of multiple branches or directories
--------------------------------------------------------------------------

USAGE
=====

.. code-block:: bash

    git all [-h] [-q] [-v] [-a] [-f] [-i INDENT] [-n] [name [name ...]]

Positional arguments
  ``name``: Names of branches or directories to iterate over

Optional arguments
  ``-h, --help``: show this help message and exit

  ``-q, --quiet``: Suppress all output

  ``-v, --verbose``: Report all messages in great detail

  ``-a, --all``: Visit non-git directories

  ``-f, --fail``: Fail immediately if any git all command fails

  ``-i INDENT, --indent INDENT``: Number of columns to indent output of commands

  ``-n, --no-run``: If set, commands will be printed but not executed

DESCRIPTION
===========

Performs <command> [argument ...] for each `name`, or over all
branches if no `name` is given.

Note that this does not handle aliases within commands and might do
unexpected things with complex commands.  Please handle with care.

DANGER
======

This is a bit janky

EXAMPLES
========

``git all - git log --oneline -5``
    Performs git log --oneline -5 for each branch in this repo

``git all * - git all - git log --oneline -5``
    Performs git log --oneline -5 for each branch in each
    directory in the current directory
