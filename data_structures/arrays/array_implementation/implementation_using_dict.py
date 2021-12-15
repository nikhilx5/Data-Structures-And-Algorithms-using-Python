class MyArray:

    def __init__(self, *args):
        self.data = {}
        self.length = 0
        for arg in args:
            self.data[self.length] = arg
            self.length += 1

    def add(self, element):
        self.data[self.length] = element
        self.length += 1

    def get(self, index):
        return self.data[index]

    # remove item at a particular index
    def remove(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1

    # remove the last element of an array
    def pop(self):
        del self.data[self.length - 1]
        self.length -= 1


arr = MyArray(10, 20, 30, 40, 50, 60)
# print("*****************")
# print(arr.length)
# print(arr.data)
# print(arr.get(2))
#
# print(arr.data)
# print("*******ADD**********")
# arr.add(50)
# print(arr.data)
# print(arr.length)
# print("*******ADD**********")
# arr.add(60)
# print(arr.data)
# print(arr.length)
# print("*******REMOVE**********")
print(arr.data)
arr.remove(2)
print(arr.data)
print(arr.length)
# print(arr.get(2))
