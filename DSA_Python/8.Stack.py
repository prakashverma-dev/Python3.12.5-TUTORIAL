# Stack Concept Implemenation using Array(we can implement using Linked List, bit lengthy or slow) : -

# A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.


# Stack Over Flow : When Stach is completely fulled, and if we try to perform Stack push operation, then stack DS will throw an error, called as 'StackOverFlow'.
# Stack Under Flow : When stack get empty or It is empty and if we try to perfom Stack POP Operation, then we stack DS will throw an arror called as 'StackUnderFlow'.


'''

# Stack Operations : Stacks support a small set of basic operations, all of which run in O(1) time:

i) isEmpty(): checks if the stack is empty
ii) size(): returns the number of elements in the stack
iii) top() / peek(): shows the top element without removing it
iv) push(a): adds an element a at the top
v) pop(): removes the top element.


Stacks can be implemented by using arrays or linked lists.


Stack Good Example : Our Browser maintain history of all pages we visit via stack Data Sturture and whenever we press back arrow, It just Pop the last data stored in the stack and show again to us, one by one the last pages each time; which follows LIFO(Last In First Out).

Push/Pop Operation of Element in Stack : Order of Constant Time Operation i.e O(1)/ Constant Time Complexity.
Search Element by value : Order of n tme Opration i.e O(n) .


# Use Cases of Stack :-

i) FUnction calling in any Programming Language is managed using stack. In other words, wheneever A function call another functin compiler of that programming language uses internally a stack to maintain the history.

ii) In any editor, Undo(Ctrl +Z) functionality uses stack to track and undo the last operation we did. Ex: Mircrosoft Paint, VS code, Execel, Google Docs etc.

Common Stack Applications
Stacks are used in many real-world scenarios:

Undo/Redo operations in text editors
Browser history (back/forward)
Function call stack in programming
Expression evaluation


'''

#a) Stack Implementation using Direct List : -
stack = [] # Created a Stack using Python List

# Stack Push Operation -
stack.append("https://www.cnn.com/") # First page I visited.
stack.append("https://www.cnn.com/world")  # Second Page I Visited.
stack.append("https://www.cnn.com/india") # Third Page I visited.
stack.append("https://www.cnn.com/china") # Fourth Page I visited.

# POP Operation -

print(stack.pop()) # https://www.cnn.com/china (gives the last link we visted)
print(stack.pop()) # https://www.cnn.com/india (gives the previous last link we visted)

#Peep Operation - Just to see current last eleemnt from stack
print(stack[-1]) # "https://www.cnn.com/world"

# size Operation - 
print(len(stack))






#b) Stack Implementation using Core way/Using Class and object : -
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        # return self.stack.append(data)
         self.stack += [data]         

    def pop(self):  
        if len(self.stack) == 0:
            raise Exception("Stack Underflow!") # "stack Overflow when we try to push items after stack is fulled! "
        else:
            return self.stack.pop() 
        
    def peek(self):
        if self.isEmpty == True:
            return "Stack is Empty"
        else :
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0 # Return True and False
    
    def size(self):
        return len(self.stack)
    

# Lets create a stack /Stack Object Creation -

s1 = Stack()
s1.push(2)
s1.push(-1)
s1.push(5)
# s1.pop()
# s1.pop()

print(s1.stack)  
print(s1.isEmpty())
print(s1.size())
print(s1.peek())


#c) Stack Implementation using LinkedList : -







#c) Stack Implementation using LinkedList : -
