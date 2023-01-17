# Jan 12
import random
from words import words
def get_valid_words(words):
    word = random.choice(words) # randomely chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word           # we're going to uppercast all our letters, so this should actually be: 
                          # return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letter:
            word_letters.remove(user_letter)
    elif user_letter in used_letters:
        print('You have already used that character.Please try again.')
    else:
        print("Invalvid character. Please try again.")


user_input = input('Type something: ')
print(user_input)