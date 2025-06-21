print("Hello World !!")
print("*"*10)

x = 1
y = 2
unit_price = 3
rating = 4.99
is_published = False
course_name = "Python Prograaming"

message = '''

Hi John


This is Prakash


We learning Python Progamming, Congrats!!


'''

print(message)


message2 = "Python Progamming"
print(len(message2))  # length of the string by inbuilt len() function of python
print(message2[0])  # P
print(message2[-1])  # g

# Slice string -

# Slice or extract upto 3 character means get upto index=2 string i.e index=3 is not included.
print(message2[0:3])

print(message2[0:])  # upto last index value get.
print(message2[:3])  # upto 2nd index value get.
print(message2[:])  # copy of the original string.


check = """ 
Hi John ,
this is Prakash


Blah Blah....

"""

print(check)

ms="Python Programming";
print(ms[0:3])

print("My name is \"Prakash\" Verma")  #My name is "Prakash" Verma
print("Python \"Programming"); # Python "Progamming


first="Prakash"
last="Verma"
full=first+" "+last  #string formatted.
print(full)

#better way of string formatted - can use formate string(f or F formate string)

full=f"{first} {last} 2"
print(full)

# Note: In Format String, we can put any valid express inside curly braces to  get executed, could variable value or direct python express.

full=print(f"{len(first)} {last} 3")

full=print(f"{len(first)} {last} {4+5} 4")

first.upper()
print()

