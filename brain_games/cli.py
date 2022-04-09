"""CLI Functions."""

import prompt


def welcome_user():
    """
    Return welcome string.

    Returns:
        str
    """
    name = prompt.string('May I have your name? ')
    return 'Hello, {name}!'.format(name=name)
