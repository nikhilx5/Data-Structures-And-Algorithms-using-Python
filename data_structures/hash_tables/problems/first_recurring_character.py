"""
Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
output = 2
"""


class FirstRecurringChar:

    def first_recurring(self, nums: list[int]):

        dict_map = {}
        for i, num in enumerate(nums):
            if num not in dict_map.keys():
                dict_map[num] = i
            else:
                print(dict_map)
                return num
        print(dict_map)
        return None


obj = FirstRecurringChar()
print(obj.first_recurring([2, 5, 4, 6, 0, 8, 9, 9, 4]))
