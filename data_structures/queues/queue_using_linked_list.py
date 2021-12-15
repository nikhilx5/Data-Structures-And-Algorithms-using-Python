class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Queue data structures are FIFO : First In First Out
    so if 10 <-- 20 <-- 30 <-- 40, 10 was added to the queue first so it will be the first element to be removed

    """
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def print_queue(self):
        curr_node = self.front
        for i in range(self.length):
            print(curr_node.value, end=" ")
            curr_node = curr_node.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.back = self.front
            self.length += 1
        else:
            self.back.next = new_node
            self.back = new_node
            self.length += 1

    def dequeue(self):
        """
        remove element at the start of the queue
        :return: None
        """
        self.front = self.front.next
        self.length -= 1

    def peek(self):
        """
        return the first person in the list
        :return: None
        """
        return self.front.value


obj = Queue()

obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(50)

obj.print_queue()

obj.dequeue()
print("\n")
obj.print_queue()

print("\n")
print(obj.peek())

obj.dequeue()
print("\n")
obj.print_queue()