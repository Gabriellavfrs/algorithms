def is_palindrome_iterative(word):
    if not word:
        return False

    middle = len(word) // 2
    low_index = len(word) - 1
    for high_index in range(middle):
        if word[high_index] != word[low_index - high_index]:
            return False

    return True
