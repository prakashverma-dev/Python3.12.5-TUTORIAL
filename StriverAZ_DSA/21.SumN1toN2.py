'''  

# Intuition : Find Consecutive sum from N1 to N2 natural number -

Normal -
1 + 2 + 3 + 4
n1 = 1
N2 = 4

no of terms i.e feqquency = n or (n2-n1+1) = (4-1+1) = 4

sum = (first number + last number) * (no of terms/2)

sum =  n*(n+1)/2



'''


#Approch1 : sum of from n1 to n2 consecutive numbers  -
# Time Complexity : O(n)
# Space Complexity : O(1)

def sumn1n2(n1,n2):

    sum = 0
    for i in range(n1, n2+1):

        sum += i

    return sum 

print(sumn1n2(4,9))




#Approch2 : Using Formula : -
# Time Complexity : O(1)
# Space Complexity : O(1)

# 1,2,3,4 
# n = 4 = (4-1+1)

def summ(n1,n2):

    sum = 0
    firstNo = n1
    lastNo = n2
    freqency = (n2-n1+1) # no of terms

    sum = (firstNo + lastNo) * (freqency) //2

    return sum 

print(summ(4,9))