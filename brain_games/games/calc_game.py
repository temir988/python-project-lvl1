"""Logic for brain-calc game."""

import random

from brain_games.games.common_game import get_answer, run_game

OPERATIONS = ['+', '-', '*']


def calc_game():
    """Game function for brain-calc."""
    run_game(game_step)


def game_step():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operation = random.choice(OPERATIONS)

    title = 'What is the result of the expression?'
    question = "{n1} {op} {n2}".format(n1=num1, n2=num2, op=operation)
    answer = get_answer(question, title)
    correct_answer = eval(question)

    return int(answer), correct_answer
