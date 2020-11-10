import random

def load_words(file_path, difficulty_level=4): #default difficulty level = 4
    list_of_words = []

    with open(file_path, 'r') as file:
        file_content = file.read()
        splited_sequence = file_content.split("\n")
        for word in splited_sequence:
            if len(word) > difficulty_level:
                list_of_words.append(word)

    return list_of_words

def load_words_m(file_path, difficulty_level=4): #default difficulty level = 4
    list_of_words = []

    with open(file_path, 'r') as file:
        file_content = file.read()
        splited_sequence = file_content.split("\n")
        end_condition = len(splited_sequence)
        start = 0
        while start < end_condition: #dynamic condition - can't be done with for loop
            if splited_sequence[start] < difficulty_level:
                splited_sequence.pop(start)
                end_condition -= 1
            else:
                start += 1

    return list_of_words

def get_random_word(list_of_words):
    random_word = ''

    random_index = random.randint(0, len(list_of_words))

    return list_of_words[random_index]

def display_progress(list_of_missed_char, guessing_so_far):
    print("Missed characters: [{}]".format(",".join(list_of_missed_char)))
    input_char = input("Guess the word:")

    return input_char , len(input_char) == 1 and not input_char.isdigit()

def is_valid_letter(seq_of_letters):
    #return value if condition else return another value
    return True if len(seq_of_letters) == 1 and not seq_of_letters.isdigit() else False

def get_char_position_in_word(word, char):
    indices = []
    for i in range(len(word)):
        if char == word[i]:
            indices.append(i)
    
    return indices