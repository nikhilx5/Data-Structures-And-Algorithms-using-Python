"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

"""


# brute force solution to check every combination
# time complexity: O(n^2), space complexity: O(n)
def two_sum(input_array: list[int], target: int) -> list[int]:
    for i in range(len(input_array)):  # O(n)
        for j in range(i + 1, len(input_array)):  # O(n)
            if input_array[j] == target - input_array[i]:
                return [i, j]


# using hashmap - time complexity: O(n), space complexity: O(n)
# basically for each element, we're subtracting that element from target value and checking if the different exists
# in a hashmap or not. If the different doesn't exists then we add it to the hashmap, however if the diff exists in
# hashmap then that means that current number and difference number are the 2 elements that's sum is equal to target
# we return the difference number index and current number index.
# we use enumerate so that we get the number along with its index which we use to return along with the other number
def two_sum_2(nums: list[int], target: int) -> list[int]:
    values_dict = {}  # value: index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in values_dict.keys():
            return [values_dict[diff], i]
        else:
            values_dict[n] = i


print(two_sum([3, 2, 4], 6))
print(two_sum_2([2, 7, 11, 15], 9))
