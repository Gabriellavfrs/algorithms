def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if low_index == high_index or low_index == high_index - 1:
        return word[low_index] == word[high_index]
    else:
        isEqual = word[low_index] == word[high_index]
        return isEqual and is_palindrome_recursive(
            word, low_index + 1, high_index - 1)
