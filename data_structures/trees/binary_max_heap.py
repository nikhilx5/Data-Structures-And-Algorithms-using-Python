"""
    - Heaps are type of tree which are always the complete binary tree meaning there should not be any nodes left
    - There are 2 types of Heaps: Maxheap and Minheap
        - Maxheap: a given node is always GREATER than all its descendant nodes
        - Minhead: a given node is always SMALLER than all its descendant nodes
    - Duplicates are allowed in Heap contrary to Binary tree where duplicates are not allowed
    - Heaps are represented mostly as an Array in most algorithms
    - Formula to represent heap in an array is:
        node = i
        left_node = 2 * i
        right_node = (2*i) + 1
    - In binary heap, elements are inserted from left to right
    - Heap is not useful for searching purposes
    - Height of Binary Heap is always Log N (meaning it won't increase un-necessarily"
    - getMax(): It returns the root element of Max Heap. Time Complexity of this operation is O(1).
    - extractMax(): Removes the maximum element from MaxHeap. Time Complexity of this Operation is O(Log n)
      as this operation needs to maintain the heap property (by calling heapify()) after removing root.
    - insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree.
    If new key is smaller than its parent, then we don’t need to do anything. Otherwise,
    we need to traverse up to fix the violated heap property.

"""
import sys


class MaxHeap:

    # The constructor initializes the heap with a maxsize entered by the user, size set to 0, all the elements of
    # heap set to 0
    # For the sake of easier calculation of parent and child nodes, we do the indexing from 1 instead
    # of 0. So we fill the 0th index of heap with a garbage value
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = sys.maxsize

    def left_child_pos(self, pos):
        return 2 * pos

    def right_child_pos(self, pos):
        return (2 * pos) + 1

    def swap(self, fpos, lpos):
        self.heap[fpos], self.heap[lpos] = self.heap[lpos], self.heap[fpos]

    # Method to insert a node in the heap. First we increment the size of heap by 1 and insert the element at the end
    # Inserting at the end of the heap will violate the max-heap rule that all max elements should be higher than lower
    # number elements
    # We have to check if the inserted element is greater than its parent(pos: size/2). if inserted element is greater
    # than parent then we swap both of them and keep checking it until we reach at the root node
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element
        current = self.size
        # check if the element inserted is greater than its parent
        while self.heap[current] > self.heap[current // 2]:
            self.heap[current], self.heap[current // 2] = self.heap[current // 2], self.heap[current]
            current //= 2

    def remove_max(self):
        """
            In Binary heap, we always delete the root element
            steps to delete and re-arrange/sort binary max heap
            1. Replace the smallest element with the root element
            2. compare the child of root node to find the greater element
            3. swap the greater element with the root node
            4.

        :return:
        """
        popped_root_node = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1
        self.heapify(1)  # First, we always heapify root node whose index = 1
        return popped_root_node

    # this method will be called whenever heap property is disturbed and heap needs to be balanced
    # We check if the concerned node is not the leaf node or not the first node. If it is, then no need to do anything
    def heapify(self, position):

        # all leaf nodes are at the 2nd half of the array. If the position passed is at the 2nd half of the array,
        # we don't do anything
        if not self.size // 2 < position < self.size:

            # check if the node is less than any of the left or right child
            if self.heap[position] < self.heap[self.left_child_pos(position)] or \
                    self.heap[position] < self.heap[self.right_child_pos(position)]:

                # check if the left node is greater than right node. If so, swap the node with left node
                if self.heap[self.left_child_pos(position)] > self.heap[self.right_child_pos(position)]:
                    self.swap(position, self.left_child_pos(position))
                    self.heapify(self.left_child_pos(position))

                # else if right child is greater than left child then swap node with the right child
                else:
                    self.swap(position, self.right_child_pos(position))
                    self.heapify(self.right_child_pos(position))

    def print_heap(self):
        for i in range(1, (self.size // 2) + 1):
            print(
                f"Parent: {self.heap[i]} , Left Child is: {self.heap[2 * i]}, Right Child is: {self.heap[(2 * i) + 1]}")


if __name__ == "__main__":
    my_heap = MaxHeap(15)
    my_heap.insert(5)
    my_heap.insert(3)
    my_heap.insert(17)
    my_heap.insert(10)
    my_heap.insert(84)
    my_heap.insert(19)
    my_heap.insert(6)
    my_heap.insert(22)
    my_heap.insert(9)

    my_heap.print_heap()
    print(my_heap.heap)
    print("**************")
    print(my_heap.remove_max())
    print(my_heap.heap)
    my_heap.print_heap()

    print("**************")
    print(my_heap.remove_max())
    print(my_heap.heap)
    my_heap.print_heap()

"""
                84
       22              19 
         
  17       10      5       6
    
3       9

After 1st heapify:

                22
       17              19 
         
  9       10      5       6
    
3  

After 2nd heapify:

                19
       17              6 
         
  9       10      5       3

"""
