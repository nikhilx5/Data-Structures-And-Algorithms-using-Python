"""
10 --> 5 --> 1
Linked list basically is a sequence of nodes which has 2 elements, head and tail.
At the time of initialization, head and tail will be the same
- Head element will contain 2 things: value (data) and pointer to the next element
- Tail element will contain 2 things: value (data) and pointer to the next element as NULL


we can initialize linked list by passing either value or no value (ll = LinkedList() / LinkedList(10))


"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.__dict__)


class LinkedList:

    # constructor to initialize linked list without any element
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    # print the elements of the linked list
    def print_list(self):
        if self.head is None:
            return "List is Empty"
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next

    # adding data at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # adding data at the start of the list
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    # insert data at a specified position in a linked list
    def insert(self, position, data):
        i = 0
        # if position is 0, insert the element at the head of the list
        if position >= self.length:
            if position > self.length:
                print(f"Invalid position - {position}, Inserting at the end of list")
            self.append(data)
        elif position == 0:
            self.prepend(data)
            return f"Added element at position {position}"
        else:
            new_node = Node(data)
            temp_node = self.head
            # Here we're iterating until position - 1 because temp_node is moving to next node. For example, if
            # position is 3 then range will go from 0 to 1 and for each iteration, temp node will be at node 3
            # because in each iteration, we're moving temp_node to next node so in iteration 0, temp node is at 1
            # and at iteration 1, temp node will be at node 2.. From node 2 we can begin inserting logic
            for i in range(position - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1

    # remove element at a specified position
    def remove_node_by_position(self, position):
        temp_node = self.head
        if position == 0:
            self.head = self.head.next
            # if head is the only element then assign tail as head node as well
            if self.head.next is None or self.head is None:
                self.tail = self. head
            self.length -= 1
        elif position >= self.length:
            print(f"position {position} is greater than or Equal to the length of the list: {self.length}, "
                  f"Removing element at the end of the list")
            for i in range(self.length - 1):  # O(n)
                if i == self.length - 2:
                    self.tail = temp_node
                    temp_node.next = None
                    self.length -= 1
                else:
                    temp_node = temp_node.next
        else:
            for i in range(position - 1):
                temp_node = temp_node.next
            temp_node.next = temp_node.next.next
            self.length -= 1
            if temp_node.next is None:
                self.tail = temp_node

    # remove node with a specified value
    def remove_node_by_value(self, data):
        temp_node = self.head
        if data == self.head.data:
            self.head = self.head.next
            self.length -= 1

        # for i in range(self.length - 1):
        #     if temp_node is self.tail:
        #         break
        #     elif data == temp_node.next.data:
        #         if temp_node.next == self.tail:
        #             self.tail = temp_node
        #             temp_node.next = None
        #             self.length -= 1
        #             break
        #         else:
        #             temp_node.next = temp_node.next.next
        #     else:
        #         temp_node = temp_node.next

        while temp_node.next is not None and temp_node.next.data != data:
            temp_node = temp_node.next
        if temp_node.next is not None:
            temp_node.next = temp_node.next.next
            if temp_node.next is None:
                self.tail = temp_node
            self.length -= 1


ll = LinkedList()
ll.append(10)
ll.append(5)
ll.prepend(1)
ll.print_list()

print(ll.insert(0, 20))
print(ll.length)
print(ll.insert(6, 50))
print(ll.insert(5, 66))
ll.print_list()
print("\n")
ll.insert(3, 11)
ll.print_list()

print(f"\nLength is: {ll.length}")

ll.insert(5, 99)
ll.print_list()
print(f"\nLength is: {ll.length}")
print(f"\n{ll.tail}")

ll.remove_node_by_position(0)
ll.print_list()
print(f"\nLength is: {ll.length}")

ll.remove_node_by_position(7)
ll.print_list()
print(f"\nLength is: {ll.length}")

ll.remove_node_by_position(3)
ll.print_list()
print(f"\nLength is: {ll.length}")

print("\nUsing remove_node_by_position: 2")
ll.remove_node_by_position(2)
ll.print_list()
print(f"\nLength is: {ll.length}")

print("\nUsing remove_node_by_value: 1")
ll.remove_node_by_value(1)
ll.print_list()
print(f"\nLength is: {ll.length}")

print("\nUsing insert at index: 1")
ll.insert(1, 25)
ll.print_list()
print(f"\nLength is: {ll.length}")

print("\nUsing remove_node_by_value: 50")
ll.remove_node_by_value(50)
ll.print_list()
print(f"\nLength is: {ll.length}")