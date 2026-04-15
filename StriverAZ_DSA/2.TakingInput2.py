# Problem : In First line user given some integer value as input - 4 5 7 

values = input().split(" ") # string converted into list with splitted with a space seperated from input.
print(values, type(values))

#Suppose, In First line integer values given seperated with comma : 4, 5, 7 
values = input().split(",") # string converted into list with splitted with space seperated from input.
print(values, type(values)) 




'''  Quick Recap : -

i) name = input()  --> # For taking input as String

ii) age = int(input())  --> # Taking input as Integer

iii) salary =float(input()) --> # Taking input as Float

iv) isAdmin= bool(input()) ---> # Taking input as Boolean

v)  a,b,c= map(int,input().split()) -->  # Taking 3 space separated Integer value as Input

vi) result_list = list(map(int, input().split())) --> # Taking List as Input 


'''












