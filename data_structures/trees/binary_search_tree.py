class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    '''
        In the in
    '''

    def insert(self, value):
        new_node = Node(value)
        # check if root is null
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                else:
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left

            self.number_of_nodes += 1

    def lookup(self, value):
        """
                    18

                5           24

            2    9       20       28

        """

        current_node = self.root
        while current_node:
            if current_node is None:
                return "Node Not Found"
            if current_node.value == value:
                return f"Found - {current_node.value}"
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right

        return "Not Found"

    def remove_app1(self, value):
        # check if the root is null
        if self.root is None:
            return False

        current_node = self.root
        p_node = None
        while current_node is not None:
            if current_node.value > value:
                p_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                p_node = current_node
                current_node = current_node.right
            else:
                # value == current_node.value:
                # we have a match. apply the remove node logic

                # Option 1: check if the node is leaf node meaning it has No left and right child
                if current_node.left is None and current_node.right is None:
                    if p_node is None:  # Node to be delete is root
                        self.root = None
                        return
                    if current_node.value > p_node.value:
                        p_node.right = None
                        return f"Removed - {current_node.value}"
                    elif current_node.value < p_node.value:
                        p_node.left = None
                        return f"Removed - {current_node.value}"

                # Option 2: No right child
                # check if current_node has no right child
                # if right node of current_node is null then make the current_node.left as the child of parent node
                elif current_node.right is None:
                    if p_node is None:
                        self.root = current_node.left
                        return
                    elif current_node.value < p_node.value:
                        p_node.left = current_node.left
                        return
                    elif current_node.value > p_node.value:
                        p_node.right = current_node.left
                        return

                # Option 2: No Left child
                # check if current_node has no left child
                # if left node of current_node is null then make current_node.right as the child of the parent node
                elif current_node.left is None:
                    if p_node is None:
                        self.root = current_node.right
                        return
                    elif current_node.value < p_node.value:
                        p_node.left = current_node.right
                        return
                    elif current_node.value > p_node.value:
                        p_node.right = current_node.right
                        return

                    # Option 4: current_node has both left and right child
                    """
                        The approach can be either of the below:
                        Approach 1:
                            0. Look at the right sub-tree
                            1. Find the minimum in the right sub-tree of the current_node
                            2. Copy the value of minimum to the targeted node (current_node)
                            3. Delete the duplicate from the right subtree (node with minimum value from right subtree)
                        Approach 2:
                            1. Find the maximum in the left sub-tree of the current_node
                            2. Copy the value of maximum to the targeted node (current_node)
                            3. Delete the duplicate from the left subtree (node with maximum value from right subtree)
                    """
                # when current_node has both left and right children then we look at approach 1
                # we look at the right subtree of the current node and get del_node = current_node.right
                # we loop through until del_node.left is none.. by doing this, we basically get the lowest number
                # in the right subtree.. .
                # once we get to the lowest node, we assign its value to the current_node value so after this
                # we'll have the current_node value same as lowest node value (basically duplicates)
                # after that we just delete the duplicate node.. which is the leftmost node in the right subtree
                elif current_node.left is not None and current_node.right is not None:
                    del_node = current_node.right
                    del_node_parent = current_node.right

                    while del_node.left is not None:
                        del_node_parent = del_node
                        del_node = del_node.left

                    current_node.value = del_node.value

                    # If the node to be deleted is the exact right child of the current node
                    if del_node == del_node_parent:
                        current_node.right = del_node.right  # (del_node.right will be None)
                        return

                    # delete the duplicate left most node.
                    # check if the leftmost node has any right node,
                    # if no right node, then not then just make the p_node left node as None
                    # else, if there are right node, then make that ride node as p_node's right node
                    if del_node.right is None:
                        del_node_parent.left = None
                        return
                    else:
                        del_node_parent.right = del_node.right
                        return

        return False

    def remove_app2(self, value):
        # check if the root is null
        if self.root is None:
            return False

        current_node = self.root
        p_node = None
        while current_node is not None:
            if current_node.value > value:
                p_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                p_node = current_node
                current_node = current_node.right
            else:
                # value == current_node.value:
                # we have a match. apply the remove node logic

                # Option 1: check if the node is leaf node meaning it has No left and right child
                if current_node.left is None and current_node.right is None:
                    if p_node is None:  # Node to be delete is root
                        self.root = None
                        return
                    if current_node.value > p_node.value:
                        p_node.right = None
                        return f"Removed - {current_node.value}"
                    elif current_node.value < p_node.value:
                        p_node.left = None
                        return f"Removed - {current_node.value}"

                # Option 2: No right child
                # check if current_node has no right child
                # if right node of current_node is null then make the current_node.left as the child of parent node
                elif current_node.right is None:
                    if p_node is None:
                        self.root = current_node.left
                        return
                    elif current_node.value < p_node.value:
                        p_node.left = current_node.left
                        return
                    elif current_node.value > p_node.value:
                        p_node.right = current_node.left
                        return

                # Option 2: No Left child
                # check if current_node has no left child
                # if left node of current_node is null then make current_node.right as the child of the parent node
                elif current_node.left is None:
                    if p_node is None:
                        self.root = current_node.right
                        return
                    elif current_node.value < p_node.value:
                        p_node.left = current_node.right
                        return
                    elif current_node.value > p_node.value:
                        p_node.right = current_node.right
                        return

                    # Option 4: current_node has both left and right child
                    """
                        The approach can be either of the below:
                        Approach 1:
                            0. Look at the right sub-tree
                            1. Find the minimum in the right sub-tree of the current_node
                            2. Copy the value of minimum to the targeted node (current_node)
                            3. Delete the duplicate from the right subtree (node with minimum value from right subtree)
                        Approach 2:
                            1. Find the maximum in the left sub-tree of the current_node
                            2. Copy the value of maximum to the targeted node (current_node)
                            3. Delete the duplicate from the left subtree (node with maximum value from right subtree)
                    """
                # when current_node has both left and right children then we look at approach 1
                # we look at the right subtree of the current node and get del_node = current_node.right
                # we loop through until del_node.left is none.. by doing this, we basically get the lowest number
                # in the right subtree.. .
                # once we get to the lowest node, we assign its value to the current_node value so after this
                # we'll have the current_node value same as lowest node value (basically duplicates)
                # after that we just delete the duplicate node.. which is the leftmost node in the right subtree
                    """
                                        18
                                5                    24
                            2       9            20       28
                                        15    19                 99
                    """
                elif current_node.left is not None and current_node.right is not None:
                    del_node = current_node.left
                    del_node_parent = current_node.left

                    while del_node.right is not None:
                        del_node_parent = del_node
                        del_node = del_node.right

                    current_node.value = del_node.value

                    # If the node to be deleted is the exact left child of the current node
                    if del_node == del_node_parent:
                        current_node.left = del_node.left  # (del_node.right will be None)
                        return

                    # delete the duplicate left most node.
                    # check if the leftmost node has any right node,
                    # if no right node, then not then just make the p_node left node as None
                    # else, if there are right node, then make that ride node as p_node's right node
                    if del_node.left is None:
                        del_node_parent.right = None
                        return
                    else:
                        del_node_parent.right = del_node.left
                        return

        return False

    def print_tree(self):
        if self.root is not None:
            self.printt(self.root)
        # Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node is not None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)


bst = BinarySearchTree()
bst.insert(18)
bst.insert(5)
bst.insert(2)
bst.insert(24)
bst.insert(28)
bst.insert(20)
bst.print_tree()
print(bst.lookup(20))
print(bst.lookup(2))
bst.insert(9)
bst.insert(15)
bst.insert(99)
print(bst.lookup(9))
print(bst.lookup(99))
print(bst.lookup(299))

"""
                    18
            5                    24
        2       9            20       28
                    15    19                 99
"""
# print(bst.remove(99))
# print(bst.lookup(99))

print("*********")
print(bst.lookup(24))
print(bst.remove_app2(24))
print(f"Lookup 24: {bst.lookup(24)}")
print(f"Lookup 20: {bst.lookup(20)}")

print("*********")
print(f"Lookup 28: {bst.lookup(28)}")
print(bst.remove_app2(28))
print(f"Lookup 28: {bst.lookup(28)}")
# print(f"Lookup 20: {bst.lookup(20)}")

# print(bst.lookup(99))

