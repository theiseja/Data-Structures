import sys
sys.path.append("C:\\Users\\Jesse\\Desktop\\My Projects\\School\\Python\\Data-Structures\\doubly_linked_list")
from dll_queue import Queue
from dll_stack import Stack
print(sys.path)


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting root must exist
        # if value is < self.value
        if value < self.value:
            # if different keep moving
            if self.left is None:
                self.left = BinarySearchTree(value)
                # make a left node
            else:
                self.left.insert(value)
                # if >= then go right
        elif value >= self.value:
            # if not keep moving
            if self.right is None:
                self.right = BinarySearchTree(value)
                # make a new node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # set up a QUEUE [allows nodes to backtrack]
        # init with root node

        # while the queue is NOT empty
            # dequeue node
            # print node.value
            # enqueue node.left, node.right

        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # set up a stack [node we need to backtrack to because we haven't visited both subtrees yet]
        # init with root node

        # while stack NOT empty, one thing remains that must be backtracked through
            # pop node from stacl
            # print the node.value
            # push node.left, node.right
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
