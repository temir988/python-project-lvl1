"""Step logic for brain-gcd game."""

import random
from math import gcd
from brain_games.common_game import get_answer, run_game


def gcd_game():
    """Game function for brain-calc."""
    run_game(game_step)


def game_step():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)

    title = 'Find the greatest common divisor of given numbers.'
    question = "{n1} {n2}".format(n1=num1, n2=num2)
    answer = get_answer(question, title)
    correct_answer = gcd(num1, num2)

    return int(answer), correct_answer
