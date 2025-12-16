'''

#Data Strutures : Storing Data In Python 

i) Array : a) Static Array and b) Dynamic Array

ii) List : One kind of Dynamic Array inbuilt in python with its own defined method for LIST OPERATION (Insertion, Deletion, Updation ).

iii) Linked List : 

    a) Singly Linked List
    b) Singly Linked List
    c) Singly Linked List 

iv) Stack

v) Queue
    a) Circular Queue

vi) Tree
    a) Binary Tree
    b) Binary Search Tree









'''

# Creating Class to defined The Linked List Node Structure having one data stores and another adresss stores of another node -

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Now, Creating Objects i.e Nodes from the class -
node1 = Node(10) # 10, 20, 30, 40 are the data.
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Lets Connect all nodes with next Node Address(which we get once we defined the nodes where each node holds some random location in memory), to form a linked list -

node1.next = node2
node2.next = node3
node3.next = node4

# Our Linked List Is Ready Now, Now we can perform some operation on our created Linked List- 

# -----------------------------OPERATION ---------------------

# i) Traversal / Means Printing All LinkedList Data -

currentNode = node1 # head

# currentNode
while currentNode:
    print(currentNode.data)
    currentNode = currentNode.next   



