'''
1) # Algorithm/Solution Ways : As we know, algorithm is a step-by-step procedure, which defines a set of instructions to be executed in a certain order to get the desired output. Algorithms are generally created independent of underlying languages, i.e. an algorithm can be implemented in more than one programming language. 

Pseudo Code : Pseudo Code is a description of the steps for writing an algorithm for a problem given in simple English.

One Problem can be solved in different ways i.e different approch of algorithm.


2) #From the data structure point of view, following are some important categories of algorithms - 

    • Search : Algorithm to search an item in a data structure.
    • Sort : Algorithm to sort items in a certain order.
    • Insert : Algorithm to insert item in a data structure.
    • Update : Algorithm to update an existing item in a data structure.
    . Delete : Algorithm to delete an existing item from a data structure.


3) # Algorithm Analysis : What if I gave a problem to three students to solve it and they gave three different solutions by using different ways or algo; so now being a teacher or programmer whose solution is better and would I select, It known as Algorithm Analysis.

	So, Better Efficiency of an algorithm can be analyzed by two different factors : -

	1) Time Complexity : - The time complexity of an algorithm measures how the running time of the algorithm scales in relation to the size of the input. It's essential to note that this running time is a function of the input length and not directly dependent on the execution time of the machine where the algorithm is being executed.
	
    2) Space Complexity : The space complexity of an algorithm measures the amount of memory the algorithm requires to execute  based on the size of input.

Note : We avoid measuring efficieny of the algorithm with runtime of any program coz it could be fast or slow from machine to machine as well as we do not measure in general. We only measure using Time and Space Complexity which tells to calculate the no of steps of algorithm as per input size.

4) Asymptotic Analysis and Notations : Asymptotic analysis refers to defining the mathematical representation of algorithm run-time efficieny i.e calculates time and space complexity of an algorithm. 

Using asymptotic analysis, we can very well conclude the best case, average case, and worst case scenario of an algorithm.n

Usually, the time required by an algorithm falls under three types −

Best Case − Minimum time required for program execution.

Average Case − Average time required for program execution.

Worst Case − Maximum time required for program execution.

# Asymptotic Notations : Asymptotic notations are used to represent the complexity of an algorithm i.e Time and Space complexity of an algorithm. Following are three asymptotic notations are used to calculate the running time complexity of an algorithm -

i) O - Big Oh Notation

ii) Ω - Big omega Notation

iii) θ - Big theta Notation

Note : Here, Big Oh use to represent Worst Time Complexity, Big Omega used to Best Case Complexity and Big theta use to represent Average Case Complexity.

# Big O Notation : It is the one of the Asymptotic Notation which uses to find the worst time and space complexity of an algorithm, in term of O(..).

We follow mathematical x-y graph to represent time and space complexity where on x-axis we refer the input size of an array and on y-axis we represent how fast time grows as per input size increases.

We follow some rules for repesent in Big O notatation -

a) We express equation of time complexity in term of input.
b) We focus on bigger picture or term in the equation with dropping or removing the minor terms or parameters.



# How to calculate Time Complexity of an algorith in terms of Big O Notation : -

In short To Calculate Time Complexity : Calculate the no of steps/operations performed in an algorithm or if loop is there calcuate no of times loops occures as per input size and then express w.r.to its input size in the euquation. and Finally take the bigger picture of equation in terms of big O. 


Note : Some Short Cut to Remember Time Complexity of some specific algorithm if it follows -

 > Whenever there is -
i) One Loop in entire algorithm which runs full input size(0 to n) ---> Linear Time Complexity [O(n)]

 Equation will look like this : 5n + 1   --> O(n)

ii) Two Nested Loops inside one after another in entire algorithm which runs full input size(0 to n) ---> Quadratic Time Complexity [O(n^2)]  

 Equation will look like this : 3n^2 + 5n + 1  --> O (n^2)

iii) Three Nested Loops inside one after another in entire algorithm which runs full input size(0 to n) ---> Cubic Time Complexity [O(n^3)]

 Equation will look like this : 7n^3 + 3n^2 + 5n + 1  --> O (n^3)

iv) Input size gets half after each loop iteration in entire program(0 to n) ---> Logarithnmic Time Complexity [O(log n)]

 Equation will look like this : t = n/2 (apply log both sides) --> O (n/2) or O(logn)
                                log(t) = logn - log2
                                log(t) = logn





'''











# 1. sum and product of an array -
L = [1,2,3,4,5]
sum=0
for i in L:
    sum += i  # O(n) time 
print(sum)

product = 1
for i in L:
    product *= i  # O(n) time
print(product)

# THus, O(n+n) = O(n) Time Complexity. (As Array Size get doubled TIme will also takes double.)

# 2.Printing array Items in Pairs -
L = [1,2,3,4]
for i in L:
    for j in L:
        print(i,j)

# Here, O(n) * O(n) = 