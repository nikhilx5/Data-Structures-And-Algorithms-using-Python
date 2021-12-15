from implementation import DoublyLinkedList, Node

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(0)
doubly_linked_list.append(77)
doubly_linked_list.append(20)
doubly_linked_list.append(30)
doubly_linked_list.append(50)
doubly_linked_list.append(60)
doubly_linked_list.append(80)
doubly_linked_list.print_list()

"""

"""


def reverse(d_linked_list):
    current_node = d_linked_list.bottom
    d_linked_list.top = current_node
    print("\n")
    for i in range(d_linked_list.length):
        current_node.next = current_node.previous
        current_node.previous = current_node.next
        current_node = current_node.previous

    d_linked_list.print_list()


reverse(doubly_linked_list)
