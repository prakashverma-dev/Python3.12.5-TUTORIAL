# Input First Line : two integer value given seperated with space.


def myMainFunction():
    pass  # It return a value


# Input Handler-

arr = input().split(" ") # convert the given string into array string

# m = int(arr[0])
# m = int(arr[1])
n1,n2 = map(int, arr) # OR, Map each array item to convert into integer and destructed
print(myMainFunction(n1, n2))


# print(n1, type(n1))
# print(n2, type(n2))
