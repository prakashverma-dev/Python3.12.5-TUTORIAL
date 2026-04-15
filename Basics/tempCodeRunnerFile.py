


def summation(mylist):

    print(id(mylist)) # 2258607978368
    print("mylist :", mylist)

lst = [3,4,5,6]
print(id(lst)) # 2258607978368
print("lst:", lst)

summation(lst)

# Integer Case - Here 'x' is integer
def summ(myx):
    print(myx, id(myx))

x=3
print(x, id(x))

summ(x)

def mysum(*arr):

    print(arr)
    print("sum is :", sum(arr)) 
    print(type(arr))

mysum(2,3,4,5)