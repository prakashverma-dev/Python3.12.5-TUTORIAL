'''
# Recursion : when a function calls iteself again and again untill a specified base condition is met to stop the function calling itself, knwown as Recursion Function.

#
# Main Function
f(){                                   

f() --> function 
        itself called!

}

#Replic1 of main func -
f(){                                   

f() --> function 
        itself called!

}


#Replic2 of main func -
f(){                                   

f() --> function 
        itself called!

}


#Replic2 of main func -
f(){                                   

f() --> function 
        itself called!

}

So on...


# Infinite Recursive : When a function calls itself without any specified condition to stop it, called as infinite Recursive.'

# Stack Overflow : In Infinite Recursive case stack overflow happend, it a state where stack get over filled with function pending called.


#Recursive Function with base condition to stop it : -

# We use a 'count' variable to stop the recursive call -

count = 0
f(){

    if(count == 3){
        return; 
    }

    # Else part -
    print(count) # 0, 1, 2
    count++
    f() # Function called itself.
}


f() # main function get called.





'''

# Infinite Recursive Function Example -
def hello():
    
    print("1")
    hello() # It will get called infinitly

# hello() # RecursionError: maximum recursion depth exceeded

#Recursive Function with base condition to stop it : -


# Recursive Logic Implemenation using 'count' Variable : print 1,2,3..with increment count -

# We use a 'count' variable to stop the recursive call -
count = 0
def hello1():

    global count # look for count variable in global/that is make count variable global.
    if count == 3:
        return
    
    # Else Part 
    print(count) # 0, 1, 2
    count += 1
    hello1() # Function called itself

'''
Note : When we initialize the counter as 0 it run till one less than specified condition, i.e -

if condition, count == 3 then iteration run from 0 to 2.


''' 
hello1() # Main funtion called.

