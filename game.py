#Kaggle.com machine learning datasets and problems


import sys
#sys.path.append("/home/kareem_ahmed/Documents/Python_Workspace/Hangman Game")
print(sys.path)
import my_custom_lib

print(sys.path)

#returns list of words
words = my_custom_lib.load_words("words.txt", difficulty_level = 4)
random_word = my_custom_lib.get_random_word(words)

MAX_NUMBER_OF_TRIALS = 10
no_of_trials_so_far = 0
previously_guessed_chars = []
choosed_letters = []
win = False

print("I'm thinking of word of {} letters".format(len(random_word))
print(" ")

while (no_of_trials_so_far < MAX_NUMBER_OF_TRIALS and win == False):
    char = input("Please guess a character: ")
    if my_custom_lib.is_valid_letter(char):
        #pass #like continue
        if char in random_word:
            if char in previously_guessed_chars:
                print("You entered this before")
                no_of_trials_so_far += 1
            else:
                previously_guessed_chars.append(char)
                char_positions = my_custom_lib.get_char_position_in_word(random_word, char)
                for pos in char_positions:
                    choosed_letters[pos]
        else:
            print("Doesn't exist")
            no_of_trials_so_far += 1
    else:
        print("You have to enter one letter")
    print("")
