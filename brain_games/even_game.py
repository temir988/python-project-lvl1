"""Logic for brain-even game."""

import random

import prompt


def even_game():
    """Game function for brain-even."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))

    index = 0
    while index < 3:
        num = random.randint(0, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        answer = prompt.string('Question: {number}\n'.format(number=num))
        correct_answer = 'yes' if num % 2 == 0 else 'no'

        if answer != correct_answer:
            print(
                "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
                .format(wrong=answer, correct=correct_answer))
            print("Let's try again, {name}!".format(name=name))
            break

        print('Correct!')
        index += 1
    else:
        print('Congratulations, {name}!'.format(name=name))
