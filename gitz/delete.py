from .git import GIT
from . import git_functions


def delete(branches, remotes, git=GIT):
    """Delete locally and on zero or more remotes"""
    # Locally
    existing_branches = git_functions.branches(git=git)
    to_delete = [b for b in branches if b in existing_branches]
    if len(to_delete) == len(existing_branches):
        raise ValueError('This would delete all the branches')

    unknown_remotes = set(remotes).difference(git.remote())
    if unknown_remotes:
        raise ValueError('Unknown remotes:', *unknown_remotes)

    if git_functions.branch_name() in to_delete:
        undeleted_branch = next(b for b in branches if b not in to_delete)
        git.checkout(undeleted_branch)

    if to_delete:
        git.branch('-D', *to_delete)

    count = len(to_delete)

    # Remote branches
    for remote in remotes:
        git.fetch(remote)
        rb = git_functions.branches('-r', git=git)
        to_delete = [b for b in branches if (remote + '/' + b) in rb]
        if to_delete:
            git.push(remote, '--delete', *to_delete)
            count += len(to_delete)

    return count
