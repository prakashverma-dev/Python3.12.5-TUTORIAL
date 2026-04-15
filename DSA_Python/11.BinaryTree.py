
'''

# Binary Tree : A tree is a hierarchical data structure like we see in our comupter main folder then sub-folders etc. Binary Tree have maxupto 2 Childs ,like either 0 child or, 1 child or, 2 childs.

A Binary Tree is a type of tree data structure where each node can have a maximum of two child nodes, a left child node and a right child node.

When A node have two max two childs nodes, then -

Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, and run faster.
Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
Binary Trees can be represented as arrays, making the tree more memory efficient.


# Types of Binary Tree based on Nodes, edges -

i) Full Binary Tree : Each node must have either 0 Node or 2 Nodes; not single node.

ii) Complete Binary Tree : a) All level must be full occupied except the last level nodes. AND b) The last level has all nodes to align extreme left side.


iii) Perfect Binary Tree : a) All leaf nodes are at same level not disbalance level. b) All non-leaf node must have 2 children.

iv) Balanced Binary Tree : Height difference between left and right subTree at any node must be at max 1.

v) Degenerate Binary Child : In entire tree, Each node has only one child.


# Binary Tree Implemenation In Python : -

The Binary Tree can be implemented much like a Linked List, except that instead of linking each node to one next node, we create a structure where each node can be linked to both its left and right child nodes.

        drinks
       /      \
     hot      cold
    /   \     /    \
tea   coffee sprite fanta



Let's Implemente this Tree Data In python - We will use Class and Object -


'''

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.leftN = None
        self.rightN = None

# Let's create Objects i.e TreeNodes with assiging value to it -

drinks = TreeNode("drinks")
hot = TreeNode("hot")
cold = TreeNode("cold")
tea = TreeNode("tea")
coffee = TreeNode("coffee")
sprite = TreeNode("sprite")
fanta = TreeNode("fanta")

# Now, Lets connect all nodes with respective nodes leftNode and RightNode to form the tree -

drinks.leftN = hot
drinks.rightN = cold

hot.leftN = tea
hot.rightN = coffee

cold.leftN = sprite
cold.rightN = fanta


# So, Our Tree Data Struture is ready now, we can perform some operation on this created tree data like Data Traversal means Priting all data from tree, deletion a particular data, inserting a data to node, changing a value from node, searching a vlaue from node etc. - 

# Let's Print a direct data from Tree just like in array print(arr[0]) -

print(drinks) # We printing an object so we get the memory.
print(drinks.val) # 'drinks'

print(drinks.leftN) # We get the same addresss as below 
print(hot) # We get the same addresss

print(drinks.leftN.val) # 'hot'
print(hot.val) # 'hot'

print(drinks.leftN.leftN.val) # 'tea' 
print(drinks.rightN.leftN.val) # 'sprite' 
print(drinks.rightN.leftN.leftN.val) # None.val ; hence we get error :  AttributeError: 'NoneType' object has no attribute 'val'


'''

        drinks
       /      \
     hot      cold
    /   \     /    \
tea   coffee sprite fanta



'''
 


        
    