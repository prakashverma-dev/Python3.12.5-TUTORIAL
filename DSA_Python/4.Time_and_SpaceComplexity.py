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