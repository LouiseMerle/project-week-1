import requests
import random
import re

#define variables

'''
L.S. Very nice piece of code! Well done! The structure is clear and the general outline looks good. 
Minor improvement could be to add some comments. 

You also cleverly otained a list of words from the internet. A good practice in finding and retrieving data!
'''

'''
L.S. You can maybe add an ascii range function so that you don't have type all the letters yourself. 
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

guess_list = []

letter_choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


'''
L.S. Nice Function! 
'''

#defining functions 

def random_word():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    website_data = requests.get(word_site)
    word_list = website_data.content.splitlines()

    word = word_list[random.randint(0, len(word_list))]
    word2 = str(word)
    clean_word1 = word2.lstrip("b'")
    clean_word2 = clean_word1.rstrip("'")

    random_shizzle = clean_word2.lower()

    random_list = re.findall('[a-z]', random_shizzle)

    return random_list


def guess(input_human, random_list, guess_list):
    index = 0
    for letter in random_list:
        index += 1
        if input_human == letter:
            guess_list[index-1] = input_human         

    return guess_list
    
name = input("Hello, what's your name? ")


#start game!
while True:

    guess_list = []

    '''
    L.S. Here you could have made a copy of the alphabet list, saves some typing. 
    '''

    letter_choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    '''
    L.S. Good!
    '''

    print("Hi, welcome", name, "what a great day to play hangman!")
    
    secret_word = random_word()

    turns = len(secret_word) + 5

    for letter in secret_word:
        guess_list.append("*")
    print('Your word is:', guess_list)
    print('')

    while turns > 0:
        print('You have %d turns left' %turns)
        print('')
        turns -= 1
        print("The letters that are left to choose from: ", letter_choices)
        print('')
        human_choice = input("Which letter do you want to choose? ")
        print('')


        '''
        L.S. Yes, very good!
        '''

        if human_choice in alphabet:
            if human_choice in letter_choices:
                letter_choices.remove(human_choice)
                guess_list = guess(human_choice, secret_word, guess_list)
                print('Your word is now:', guess_list)
                print('')
                if guess_list == secret_word:
                    print("Congratualions! You won!, the word was: ", guess_list)
                    break
            else:
                print("You already chose that letter")
                print('')
                print('Your word is:', guess_list)
                continue
        else:
            print("this is not a letter, please choose a-z")
            continue

    if turns == 0:
        print("You lost!, the word was: ", secret_word)

    '''
    L.S. Yes, very good to ask the user whether he/she wants to play a second time. 
    '''

    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break

