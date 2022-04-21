"""Common game logic."""

import prompt


def run_game(step):
    name = welcome_game()

    index = 0
    while index < 3:
        answer, correct_answer = step()

        if answer != correct_answer:
            wrong_message(name, answer, correct_answer)
            break

        print('Correct!')
        index += 1
    else:
        congrats(name)


def welcome_game():
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def get_answer(question, title):
    print(title)
    return prompt.string('Question: {q}\n'.format(q=question))


def wrong_message(name, answer, correct_answer):
    print(
        "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
        .format(wrong=answer, correct=correct_answer)
    )
    print("Let's try again, {name}!".format(name=name))


def congrats(name):
    print('Congratulations, {name}!'.format(name=name))
