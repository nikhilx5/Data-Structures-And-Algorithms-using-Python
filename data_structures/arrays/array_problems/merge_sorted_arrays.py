"""
.............. Merge Sorted Arrays ..............
Given the two sorted arrays, we hav to merge them so that final result is a big sorted array.
example: [0,3,4,31] and [4,6,30] when merged gives output:
[0, 3, 4, 4, 6, 30, 31]
"""

"""
approach1: we can compare each values of the two arrays with each other and add the smaller values to a new list/array
one of the array will reach the end of its index. This means that other array has the largest element.
In such case, we can add the element of other array to the merged list
check def merge_arrays_1 for this approach

approach2: This approach is similar to approach 1 that we compare the values of both the arrays and add the smaller value to the merged array
after comparing, we can simple add any left over item from both the arrays
see def merge_arrays_2 for this approach
"""


class MergeSortedArrays:

    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        self.merged_array = []

    array1: [0, 3, 4, 31]
    array2: [4, 6, 30]

    def merge_arrays_1(self):
        i = j = flag = 0
        merged_array = []

        while not (i >= len(self.arr1) or j >= len(self.arr2)):
            if self.arr1[i] < self.arr2[j]:
                merged_array.append(self.arr1[i])
                i += 1
            else:
                merged_array.append(self.arr2[j])
                j += 1

        # after traversing through the while loop, one of the array reaches the end of the index
        # we need to know which array reaches the end  so that other arrays remaining elements can be added
        if i == len(self.arr1):
            flag = 1  # this flag tells us if we reached the end of the first array or the second array

        if flag == 1:
            for item in self.arr2[j:]:
                merged_array.append(item)
        else:
            for item in self.arr1[i:]:
                merged_array.append(item)

        return merged_array

    def merge_arrays_2(self):
        i = j = 0
        merged_array_2 = []

        if len(self.arr1) == 0:
            return self.arr2
        elif len(self.arr2) == 0:
            return self.arr1

        while i < len(self.arr1) and j < len(self.arr2):
            if self.arr1[i] <= self.arr2[j]:
                merged_array_2.append(self.arr1[i])
                i += 1
            elif self.arr2[j] <= self.arr1[i]:
                merged_array_2.append(self.arr2[j])
                j += 1

        return merged_array_2 + self.arr1[i:] + self.arr2[j:]




# msa = MergeSortedArrays([0, 3, 4, 31, 99, 234], [4, 6, 30, 82])
# print(msa.merge_arrays_1())

msa2 = MergeSortedArrays([1,3,5,7,9], [2,4,6,8,10])
print(msa2.merge_arrays_2())
