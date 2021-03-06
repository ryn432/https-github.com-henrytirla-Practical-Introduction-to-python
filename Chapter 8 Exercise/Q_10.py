"""
Write a censoring program. Allow the user to enter some text and your program should print
out the text with all the curse words starred out. The number of stars should match the length
of the curse word. For the purposes of this program, just use the“curse” words darn, dang,
freakin, heck, and shoot.
"""

from enum import Enum

class curses(Enum):
    CURSE_WORDS = ['darn', 'dang', 'freakin', 'heck', 'shoot']

def censor(message):
    user_input = input(message)
    user_input = user_input.lower()
    for i in curses.CURSE_WORDS.value:
        user_input = user_input.replace(i, '*')
    censor_input = user_input.capitalize()
    print('')
    print(censor_input)
    

def main():
    print('Welcome to the Censoring Progam.')
    print('\nThe following are curse words that will be censored: \n')
    print(' - '.join(curses.CURSE_WORDS.value))
    message = 'Enter a statement that contains these words: \n'
    censor(message)

if __name__ == '__main__':
    main()

# Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freakin try.
