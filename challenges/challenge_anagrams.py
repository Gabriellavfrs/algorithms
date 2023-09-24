def is_anagram(first_string, second_string):

    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    sort(first_list)
    sort(second_list)

    first_sorted = ''.join(first_list)
    second_sorted = ''.join(second_list)

    if not first_string or not second_string:
        return (first_sorted, second_sorted, False)

    is_anagram = first_sorted == second_sorted
    return (first_sorted, second_sorted, is_anagram)


def sort(letters, start=0, end=None):
    if end is None:
        end = len(letters)
    if (end - start) > 1:
        mid = (start + end) // 2
        sort(letters, start, mid)
        sort(letters, mid, end)
        merge(letters, start, mid, end)


def merge(letters, start, mid, end):
    left = letters[start:mid]
    right = letters[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            letters[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            letters[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            letters[general_index] = left[left_index]
            left_index += 1
        else:
            letters[general_index] = right[right_index]
            right_index += 1
