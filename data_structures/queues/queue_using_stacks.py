"""
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

"""


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    # [11, 2, 9, 44, 78]
    def push(self, x: int) -> None:
        # fist loop through all the elements of stack 1, remove and add them to stack 2
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())

        # add element to the stack 1 which is now empty after the for loop
        self.s2.append(x)

        # Now pop each element from s2 and add it to s1 with element x being the first element in s1 with above append
        # This has appended the last element at the start of the list with first appended element at the end
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        if len(self.s1) == 0:
            print("Stack is empty!")
        else:
            return self.s1.pop()

    def peek(self) -> int:
        return self.s1[len(self.s1)-1]

    def empty(self) -> bool:
        if len(self.s1) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(11)
obj.push(2)
obj.push(9)
obj.push(44)
obj.push(78)

print(obj.s1)

# removed 11 the first element from the queue
print(obj.pop())

print(obj.s1)
# peeking the next element in the queue, which is 2 after removing 11 with above Pop method
print(obj.peek())

# param_3 = obj.peek()
# param_4 = obj.empty()
