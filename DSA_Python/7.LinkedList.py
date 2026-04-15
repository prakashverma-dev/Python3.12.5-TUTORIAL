'''


# Array : To store sequence of values in array. The problem with array the size of array is fixed.

With specify  index value ---> we get fast value --> O(1)



# Linked List : We dont values in sequence manner, we store in something called as "Node/Ref/Address".

Linked List is linear data structure. We can use Linked List in place of Array.

Linked List is basically a collection of nodes.

Node is something that we can store adress and data. [d][a] ; address/a here = 700
 
[d][700];a = 500  ---->  [d][200];a=700 ---->  [d][900];a=200  ---->  [d][a];a=900     

The First Node In Linked List, we called it as hEad or head node and last node we refer or call it as tail or Tail Node.

The tail node address pointer pointing towards 'null' address. By This we can indentify it is tail node.


# Why should not use Array for some cases :-

i) Insertion and Deletion In array, we need to shift all rest items for each Insertion and deletion, i,e O(n) is Time Complexity for Write Operation. 

    hence, Write Operation we can use Linked List Data Structure. e.g : TO DO LIst : we do a lot of add and delete operation.

    Write Operation of Linked List is O(1) Constant Time Complexity coz we just break the node refer the pointer to new address node and same way for deletion we just remove the node and adjust the node reference.

    


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



