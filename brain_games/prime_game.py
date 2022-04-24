"""Step logic for brain-prime game."""

import random
from brain_games.common_game import get_answer, run_game


def prime_game():
    """Game function for brain-calc."""
    run_game(game_step)


def game_step():
    num = random.randint(0, 100)
    title = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = "{n}".format(n=num)
    answer = get_answer(question, title)
    correct_answer = is_prime(num)

    return answer, correct_answer


def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return 'no'

    return 'yes'
