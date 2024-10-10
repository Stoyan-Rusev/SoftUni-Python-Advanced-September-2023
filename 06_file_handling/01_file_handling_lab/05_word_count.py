import os

with open('05_words.txt', 'r') as words_file:
    searched_words = words_file.readline().split(' ')
    searched_words[-1] = searched_words[-1].strip()

words_dict = {}

with open('05_input.txt', 'r') as input_file:
    for line in input_file.readlines():
        line = line.split(' ')
        for word in searched_words:
            for current_word in line:
                current_word = current_word.lower()
                if word in current_word:
                    if word not in words_dict.keys():
                        words_dict[word] = 0
                    words_dict[word] += 1

print(words_dict)
