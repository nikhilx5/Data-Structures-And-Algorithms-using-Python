"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum. A subarray is a contiguous part of an array.
Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
import math


class MaxSubArray:

    """
    BRUTE FORCE APPROACH
    In outer loop, we're iterating through each element and it is giving all the possible sub-arrays until last index
    For example, in the first iteration, it gives us entire array as a sub-array until last index
    In inner loop, we calculate the current_sum by adding the current element with the next element. We then check the
    maximum of current_sum and store it in the maximum variable.
    After each inner iteration, we'll keep the maximum number of that iteration in maximum variable
    At the end of outer loop, we'll have the maximum sub-array sum that we need
    Since we're looping through 2 for loop, time complexity is O(n^2)
    """
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = -math.inf
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                maximum = max(maximum, curr_sum)

        return maximum


    def max_sub_array_2(self, nums: list[int]) -> int:
        maximum = max_sub_array = nums[0]

        for i in range(1, len(nums)):
            # Max sub array at a particular index is a sum of the maximum sub_array ending at the previous index + the element at the current index
            max_sub_array = max(nums[i], nums[i] + max_sub_array)
            maximum = max(maximum, max_sub_array)
        return maximum

obj = MaxSubArray()

# 2, 4, 2, 6, 2, 3, -1
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(obj.maxSubArray([5, 4, -1, 7, 8]))
print(obj.maxSubArray([-2,-1]))
