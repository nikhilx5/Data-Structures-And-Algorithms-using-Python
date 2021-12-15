class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def print_stack(self):
        curr_node = self.top
        for i in range(self.length):
            print(curr_node.value, end=" ")
            curr_node = curr_node.next

        print(f", Length is: {self.length}")

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.bottom = self.top
            self.length += 1
        else:
            self.bottom.next = new_node
            self.bottom = new_node
            self.length += 1

    def peek(self):
        if self.top is None:
            print("psst!! Stack is Empty")
        else:
            print(self.bottom.value)

    def pop(self):
        if self.top is None:
            print("psst! Stack is empty")
        else:
            curr_node = self.top
            for i in range(self.length - 1):
                curr_node = curr_node.next
            curr_node.next = None
            self.bottom = curr_node
            self.length -= 1


obj = Stack()
print("Peeking in Stack..")
obj.peek()

print("Pushing some data into stack")
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.print_stack()

print("Again Peeking in Stack..")
obj.peek()

print("Popping element from the Stack..")
obj.pop()
obj.print_stack()

print("Popping element from the Stack..")
obj.pop()
obj.print_stack()