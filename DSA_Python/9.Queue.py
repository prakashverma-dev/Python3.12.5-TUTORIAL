'''

# Queue : A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

Queues : Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket.

## Basic operations we can do on a queue are: 

Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue.


Queues can be implemented by using arrays or linked lists.

Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.




'''

# a) Queue Impletation Through Core way/ Class and Object -
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue Underflow!"
        else :
            return self.queue.pop(0)
        
    def peek(self):
         if self.isEmpty():
            return "Queue is empty"
         
         return self.queue[0] # Return the first element from the Queue.
    
    def isEmpty(self):
         return len(self.queue) == 0 

    def size(self):
        return len(self.queue)
    
# Create a queue
q1 = Queue()

# Enquequing the elements into the Queue DS(Enqueue means adding data from back into the DS)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

print(q1.queue)  

# Dequeueing (Means at a time removing the first element from the Queue DS)
q1.dequeue()
q1.dequeue()
print(q1.queue) 

# Size 
print(q1.size())

# isEmpty Queue(check if Queue is empty or not)
print(q1.isEmpty()) 

# Peek (Just see the first element from the Queue)
print(q1.peek()) 

#b) Queue Implementation using Direct List -

#c) Queue Implementation using Linked Lists



 