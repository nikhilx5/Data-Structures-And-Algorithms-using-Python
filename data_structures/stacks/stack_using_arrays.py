

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) != 0:
            self.stack.append(value)
        else:
            print("Stack is emtpy!")

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[len(self.stack) - 1]
        else:
            return "Stack is emtpy!"

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(len(self.stack) - 1)
        else:
            return "Stack is emtpy!"


obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)

print(obj.stack)

print(obj.peek())

obj.pop()

print(obj.stack)

print(obj.peek())
