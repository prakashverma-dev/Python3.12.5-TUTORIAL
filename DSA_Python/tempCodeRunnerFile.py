
# import time
# start = time.time()
# for num in range(1, 101):
#     print(num)
# end = time.time()
# print("Run-time of code : ", end - start )

# num = 1
# while num<=100:
#     print(num)
#     num += 1

def summation(n):

    sum = 0   # 1 operation
    for num in range(1, n+1):
        sum += num # 5 Operation (for 5 inputs size)
    return sum   # 1 Operation

print("The sum of till nth natural number : ", summation(5)) # 15

# Thus, 5 + 1+1 = 5 +2 = 5 (We concentrate on bigger picture or bigger terms)
# Here, n = 5 ---> n + 2 = n


    


        

