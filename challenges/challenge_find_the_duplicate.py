def find_duplicate(nums):
    if not nums or len(nums) < 2:
        return False

    nums.sort()

    for index in range(len(nums) - 1):
        num = nums[index]
        if type(num) == str or num < 0:
            return False

        result = binary_search(nums, num, index + 1)
        if result:
            return nums[result]
    return False


def binary_search(numbers, target, start):
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            return mid

        if target < numbers[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return False
