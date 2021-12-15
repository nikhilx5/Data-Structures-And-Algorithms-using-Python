"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
from typing import List


def move_zeroes(nums: list[int]) -> None:
    length = len(nums)
    while length > 0:
        for i in range(0, len(nums) - 1):

            if nums[i] == 0 and nums[i] < nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
        length -= 1

    print(nums)


def swap_move(array):
    z = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[z] = array[z], array[i]
            z += 1
    print(array)


def moveZeroes(nums: List[int]) -> None:
    snowBallSize = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            snowBallSize += 1
        elif snowBallSize > 0:
            t = nums[i]
            nums[i] = 0
            nums[i - snowBallSize] = t

    print(nums)


move_zeroes([0, 1, 0, 3, 12])
moveZeroes([45192, 0, -659, -52359, -99225, -75991, 0, -15155, 27382, 59818, 0, -30645, -17025, 81209, 887, 64648])
move_zeroes([45192, 0, -659, -52359, -99225, -75991, 0, -15155, 27382, 59818, 0, -30645, -17025, 81209, 887, 64648])
