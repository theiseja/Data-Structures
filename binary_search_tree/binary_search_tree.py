import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # BST was empty
            if self.value is None:
                self.value = BinarySearchTree(value)
                self.value = value
            # insert into right subtree
            elif value > self.value:
                # TBC
            # insert into left subtree:
                

    # Return True if the tree contains the value
    # False if it does not
def contains(self, target):
    
    # !. base cases:
    # target found or we hit none
    
    # 2. Recursive case
    # go down left or right subtree
        pass

    # Return the maximum value found in the tree
def get_max(self):
    # RIGHT as far as you can go
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
def for_each(self, cb):
    # 1. base case: left is None or Right is None
    
    # 2. Recursive case:
    # go left and right 
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
def post_order_dft(self, node):
        pass
