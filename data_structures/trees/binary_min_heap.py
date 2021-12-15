import sys


class BinaryMinHeap:

    # constructor to initialize a heap of a given size
    def __init__(self, max_size):
        # first we create a heap with all the element as 0, we create max_size + 1 because binary heap start at index 1
        self.heap = [0] * (max_size + 1)
        self.size = 0
        # since heap starts at index 1, we put garbage value at index 0
        self.heap[0] = -sys.maxsize - 1

    # now lets create a insert method, Inorder to insert element into heap, we first add the element at the end of the
    # array. To do that, we increase the size of array by 1
    def insert(self, element):
        self.size += 1
        self.heap[self.size] = element
        current = self.size
        while self.heap[current] < self.heap[current // 2]:
            self.heap[current], self.heap[current // 2] = self.heap[current // 2], self.heap[current]
            current //= 2

    def print_heap(self):
        print(f"Size is: {self.size // 2}")
        for i in range(1, self.size // 2 + 1):
            print(f"Parent: {self.heap[i]}, Left_child: {self.heap[2 * i]}, Right_child: {self.heap[(2*i) + 1]}")


my_heap = BinaryMinHeap(15)
my_heap.insert(10)
my_heap.insert(20)
my_heap.insert(30)
my_heap.insert(25)
my_heap.insert(5)
my_heap.insert(40)
my_heap.insert(35)

my_heap.print_heap()
print(my_heap.heap)

"""
MaxHeap output: 
    Size is: 3
    Parent: 40, Left_child: 25, Right_child: 35
    Parent: 25, Left_child: 10, Right_child: 5
    Parent: 35, Left_child: 20, Right_child: 30
    [9223372036854775807, 40, 25, 35, 10, 5, 20, 30, 0, 0, 0, 0, 0, 0, 0, 0]
Minheap output:
    Size is: 3
    Parent: 5, Left_child: 10, Right_child: 30
    Parent: 10, Left_child: 25, Right_child: 20
    Parent: 30, Left_child: 40, Right_child: 35
    [-9223372036854775808, 5, 10, 30, 25, 20, 40, 35, 0, 0, 0, 0, 0, 0, 0, 0]
"""