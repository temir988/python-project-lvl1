#!/usr/bin/env python

"""Project main script."""

from brain_games.cli import welcome_user


def main():
    """Project main function."""
    print('Welcome to the Brain Games!')
    print(welcome_user())


if __name__ == '__main__':
    main()
