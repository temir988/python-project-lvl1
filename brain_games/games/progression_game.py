"""Step logic for brain-gcd game."""

import random
from brain_games.games.common_game import get_answer, run_game


def progression_game():
    run_game(game_step)


def game_step():
    progression, correct_answer = get_progression()

    title = 'What number is missing in the progression?'
    question = "{p}".format(p=progression)
    answer = get_answer(question, title)

    return int(answer), correct_answer


def get_progression():
    length = random.randint(5, 15)
    step = random.randint(1, 10)
    start = random.randint(1, 100)
    hidden_index = random.randint(0, length - 1)

    progression = [*range(start, start + length * step, step)]
    hidden_elem = progression[hidden_index]
    progression[hidden_index] = '..'
    return " ".join(map(str, progression)), hidden_elem
