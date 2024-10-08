def palindrome(word, index):
    while index < len(word) // 2:
        if word[0+index] != word[-1 - index]:
            return f'{word} is not a palindrome'
        return palindrome(word, index + 1)
    return f'{word} is a palindrome'


print(palindrome("abcba", 0))
