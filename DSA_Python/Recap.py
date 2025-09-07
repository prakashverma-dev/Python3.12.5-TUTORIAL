#i) Looping for-in Over range() : 
for num in range(0,11):
    print(num) # 0 1 2 3 ... 10

# ii) for-in over list :
for item in [3,5,6,1]:
    print(item) # 3 5 6 1  #When we need just the items not index.  

# iii) for-in over list with printing index as well as items using enumerare method -
for index, item in enumerate([3,5,6,1]):
    print(index) # 0 1 2 3
    print(item) # 3 5 6 1

# using range() method -
myarr = [3,4,6,1] # to look like other languages.
for i in range(len(myarr)):
    print(i)
    print(myarr[i])  

myarrr = [3,4,5,6]
n = len(myarrr) #size of an array
for i in range(0,n):
    print(i) # 0 1 2 3
    print(myarrr[i]) # 3 4 5 6      

# Note : Same way we loop over an string with its each character and indexing.


# iv) Looping Reverse/Decrement Iterating over :-
# a) range() -
for num in range(11,0, -1): # We need to specify negative value.    
    print(num) #11, 10, 9, 8 ...3, 2, 1
    
# b) over list -
for item in reversed([3,4,5,6]):
    print(item) # When we need just the items not index.

myarrr = [3,4,5,6]
n = len(myarrr) #size of an array
for i in range(n-1 , -1 ,-1):
    print(i) # 3 2 1 0
    print(myarrr[i]) # 6 5 4 3

# Note : It is very important here, coz n-1 means index start from array size one less than to till zero index(we need to take one more step, so we added -1 and specified lastly -1 for decrement operation)    




