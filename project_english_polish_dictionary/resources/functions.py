"""This file contains functions used in project english-polish dictionary"""


from resources.english_polish_dictionary import eng_pol_dict
from resources.BColors import BColors
import random


#Variables
username = ''
correct_answers = 0
all_answers = 0

def get_random_word():
    """Pick and return random word from dictionary"""
    random_word = random.choice(list(eng_pol_dict.keys()))
    return random_word


def start_game():
    """Welcome user and start game"""
    global username
    print('Welcome to the game for learning English!')
    username = input('Please type your username and press enter: ')
    print(f'Hello {username.title()}!')
    print('Write polish translation for word which you see on the screen and press enter.'
          '\nPress "q" to quit.'
          '\nPress "s" for statistics.'
          '\nPress "r" for reset game.')


def ask_for_answer():
    """Ask user to give correct translation for word and delete that used word from dictionary"""
    global all_answers
    global correct_answers
    i = 0
    word = get_random_word()
    length = len(eng_pol_dict[word])
    answer = input(f'{word}: ')

    if answer == 'q':
        return answer

    while answer == 's' or answer == 'r':
        if answer == 's':
            display_statistics()
        elif answer == 'r':
            reset_game()
        elif answer == 'q':
            return answer

        answer = input(f'{word}: ')

    if answer in eng_pol_dict[word]:
        print(BColors.OKGREEN + 'OK' + BColors.ENDC)
        correct_answers += 1
    else:
        print(BColors.FAIL + 'NOK' + BColors.ENDC)

    for translation in eng_pol_dict[word]:
        if i >= length - 1:
            print(translation)
        else:
            print(translation, end=', ')
            i += 1

    # delete used word from dictionary
    del eng_pol_dict[word]
    all_answers += 1


def display_statistics():
    """Display statistics of current game on the screen"""
    correct_percent = 0
    if all_answers > 0:
        correct_percent = correct_answers/all_answers * 100
    print(f'Correct answers: {correct_answers} out of {all_answers} which is {correct_percent:.0f} percent')


def stop_game():
    """Set of methods for game ending"""
    display_statistics()


def reset_game():
    pass