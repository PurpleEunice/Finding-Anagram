# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    # [assignment] Add your code here

    word = word.lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

    return True

