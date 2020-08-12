"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        #if the value being passed is less than the current value, then we need to go left
        if value < self.value:
            if not self.left: #if there is no left value, then wrap our value in the node class
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value: #we could do just and else, but we want our duplicate nodes to go right so we have to make and elif
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass

        #check to see if target is current value
        # if target == self.value:
        #     return True
        #start checking branches
        if target < self.value:
            if self.left is None:
                #if not, then the target isn't in the tree
                return False
            elif self.left.value == target:
                #otherwise, we've found our target
                return True
        #checking the right branch
        elif target > self.value:
            #any more right branches?
            if self.right is None:
                return False
            elif self.right.value == target:
                return True

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
#     def in_order_print(self):
#         pass

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
#     def bft_print(self):
#         pass

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     def dft_print(self):
#         pass

#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self):
#         pass

#     # Print Post-order recursive DFT
#     def post_order_dft(self):
#         pass

# """
# This code is necessary for testing the `print` methods
# """
# bst = BinarySearchTree(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
