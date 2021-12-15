class MyArray:

    # initialize array
    def __init__(self, *args):
        self.data = []
        self.length = 0
        for value in args:
            self.data.append(value)
            self.length += 1

    # get element at index value
    def get(self, index):
        try:
            return self.data[index]
        except IndexError:
            print("Index is not found!")

    # add element to an array
    def add(self, element):
        self.data.append(element)
        self.length += 1

    # remove element at a particular index from an array
    def remove(self, index):
        self.data.pop(index)
        self.length -= 1


# arr = MyArray()
# adding elements to an array
# arr.add(10)
# arr.add(20)
# arr.add(30)
# arr.add(40)
# arr.add(50)
# arr.add(60)
# arr.add(70)
# # get element at index 3
# print(arr.get(3))
# # get the length of an array
# print(arr.length)
# # remove element at a particular index
# arr.remove(3)
# print(arr.get(3))
# print(arr.length)

arr2 = MyArray(10, 20, 30, 40, 50)
print(arr2.length)
print(arr2.data)

print("**************")
arr3 = MyArray()
print(arr3.length)
print(arr3.data)

print("**************")
# get element at index 3
print(f"Element at arr2 index 3 is: {arr2.get(3)}")
# remove element at a particular index
print(f"Removing element of arr2 at index 3")
arr2.remove(3)
print(f"arr2 data after remove is: {arr2.data}")