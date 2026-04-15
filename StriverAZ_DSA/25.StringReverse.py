'''   
Q. # Reverse an String : - General Approch and Recursive Approach -


#1) General Approches :- using for-loop and while loop -

i) Basic: with O(n) Space Complexity : taking newStr = "" as extra storage for adding string char from right side till left.

Time Complexity: O(n), as every character needs to be processed once to be included in the new string.
Space Complexity: O(n), as a new string of size 'n' is allocated in memory to store the reversed characters. 


Note : We cannot perform swappong operation from LeftP to RightP using two pointer concept or one pointer coz we canot change string within it that string does not allow assign character.

As, Strings are not mutable in Python means you cannot modify characters by index directly.

s = "hello"
s[0] = 'o'   # Error ❌ NOT work:


NOte : But we can just check if first and last chracter is same or not using two pointer conept and single pointer.

Other, We could convert string into list/array perform all "Array Reversal" and then lastly convert it back to string as final output.

You can convert string → list → swap → join back.


# Two Pointer Swapping Method after string converted into list -

s = "hello"
lst = list(s)      # convert to list (mutable)

i = 0
j = len(lst) - 1

while i < j:
    lst[i], lst[j] = lst[j], lst[i]   # swap
    i += 1
    j -= 1

rev = "".join(lst)
print(rev)

Note : ⭐ Time Complexity -
Time → O(n)
Space → O(n) (because a new list created)




'''

# i) BASIC : using for-loop with temp storage space -
# Time Complexity : O(n)
# Space Complexity : O(n)

def reverseString(str):

    print(id(str))

    n = len(str)
    newstr = "" # We creating a new string 

    for i in range(n-1, -1, -1):
        # print(i, name[i])

        newstr = newstr + str[i]

    return newstr # Reversed new string

name = "Prakash"
print(id(name))
print(reverseString("Prakash"))



# Same using While loop -
s = "hello"
rev = ""
i = len(s) - 1 # From back to front coming and storing all char -

while i >= 0:
    rev += s[i]
    i -= 1

print(rev)





# ii) Converting String into list and joins back as String -
# Note : ⭐ Time Complexity -
# Time → O(n)
# Space → O(n) (because a new list created)

s = "hello"
lst = list(s)      # convert to list (mutable)

i = 0
j = len(lst) - 1

while i < j:
    lst[i], lst[j] = lst[j], lst[i]   # swap
    i += 1
    j -= 1

rev = "".join(lst)
print(rev) 







# -------------------------------------------------------------------------------

# Note : To Convert String into LIst and then JOins back to String as Final Output -


s = "hello how are you"

# Mainly two ways mostly we gonna use -

#a. To converts string into a list of individual characters : string becomes mutable object now -
lst = list(s)   

#b. To convert string to list with bydefault a white space seperator provided i.e " " : : string becomes mutable object now -
lst2 = s.split() 

print(lst) # ['h', 'e', 'l', 'l', 'o', ' ', 'h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u']
print(lst2) #  ['hello', 'how', 'are', 'you']

# To joins back to String -
str1 = "".join(lst)
str2 = " ".join(lst2) # With one space

print(str1)
print(str2) 








