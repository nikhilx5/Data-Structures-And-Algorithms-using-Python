class Node:

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def print_list(self) -> None:
        if self.head is None:
            print("List is empty!")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.value, end=" ")
                current_node = current_node.next

    # add element at the end of the list
    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            new_node.next = None
            self.tail = new_node
            self.length += 1

    # add element at the start of the list
    def prepend(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.head.next = None
            self.length += 1
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node.next
            self.length += 1

    # insert value at a particular index
    # 99 50 10 20 30
    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index >= self.length - 1:
            if index > self.length:
                print("Index is greater than length, appending at the end of the list")
            self.append(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.previous = new_node
            current_node.next = new_node
            new_node.previous = current_node
            self.length += 1

    # remove element from a particular position
    def remove(self, position):
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            self.length -= 1
        elif position >= self.length:
            for i in range(self.length - 2):
                current_node = current_node.next
            self.tail = current_node
            current_node.next = None
            self.length -= 1
        else:
            for i in range(position - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            current_node.next.next.previous = current_node
            self.length -= 1


# We will import this file while reversing a linked list. So we must make sure that it runs only
# when it is the main file being run and not also when it is being imported in some other file.
if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.print_list()

    print("Appending 10")
    dll.append(10)
    dll.print_list()

    print("\nPrepending 50:")
    dll.prepend(50)
    dll.print_list()

    print("\nAppending 20:")
    dll.append(20)
    dll.print_list()

    print("\nAppending 30:")
    dll.append(30)
    dll.print_list()

    print("\nInserting 77 at index 2:")
    dll.insert(2, 77)
    dll.print_list()

    print("\nInserting 0 at index 1:")
    dll.insert(1, 0)
    dll.print_list()

    print("\nInserting 44 at index 4:")
    dll.insert(4, 44)
    dll.print_list()

    print("\nremoving 44 at index 4:")
    dll.remove(4)
    dll.print_list()

    print("\nremoving 10 at index 2:")
    dll.remove(2)
    dll.print_list()

    print("\nremoving element at index 0:")
    dll.remove(0)
    dll.print_list()

    print("\nremoving element at the end:")
    dll.remove(4)
    dll.print_list()
