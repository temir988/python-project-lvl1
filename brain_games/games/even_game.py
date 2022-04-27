"""Logic for brain-even game."""

import random

from brain_games.games.common_game import get_answer, run_game


def even_game():
    """Game function for brain-even."""
    run_game(game_step)


def game_step():
    num = random.randint(0, 100)
    title = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = '{number}'.format(number=num)

    answer = get_answer(question, title)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return answer, correct_answer
