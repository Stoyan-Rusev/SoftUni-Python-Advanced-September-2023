symbols_to_change = {"-", ",", ".", "!", "?"}

with open('01_text.txt', 'r') as f:
    lines_list = f.readlines()
    even_lines = [line for line in lines_list if lines_list.index(line) % 2 == 0]
    for current_line in even_lines:
        current_line = current_line.split()
        for word in current_line:
            for ch in word:
                if ch in symbols_to_change:
                    new_word = word.replace(f'{ch}', '@')
                    word_index = current_line.index(word)
                    current_line[word_index] = new_word
                    word = new_word
                elif ch == '\n':
                    new_word = word.replace(f'{ch}', '')
                    word_index = current_line.index(word)
                    current_line[word_index] = new_word
                    word = new_word

        print(*current_line[::-1])
