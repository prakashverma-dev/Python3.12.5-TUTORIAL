'''
# File I/O In Python / File handling In Python : -

Python can also be used to  some operations on a file like READ, WRITE i.e CREATE, Update and Delete Data that is known as File Handling in programming languges. 

# Types of all Files : - Files used to store any data for for long term saving data without loosing it unlike if it get into RAM memory(which is volatile in nature, data get    earased once we re-start out pc.)

All the files like .pdf, .png, .py etc gets saved into our pc system either into SSD or HHD.

Note : A File can be divided into two main broad types : -

i. Text Files : .txt, .docx, .log etc. (Here Data stored in form of characters)
ii. Binary Files : .mp4, .mov, .png, .jpeg etc. (Here Data stored not in form characters )

Note : Here, Text Files and Binary Files once we work on it and data get saved into our memory, it saved at the end in bits Data(0 and 1).


In Python File Handling or File I/O we generally going to do read file, write file, update file and delete file from our system related.


## Basic Operation on a File : Open File ---> Read File ----> Close File (for good programmer)

We have to open a file before reading it or writing it -

f = open("file_name", "mode") ---> open() function takes two parameters;

filename(Required) - Specify the file complete path correctly as per local system directory to work with. 
Ex: sample.text or demo.docx 

mode(Optional)  - Allow how the file would be open in any mode like 'r', 'w', etc. and Default mode is "r" if we do not mention any.

There are other modes for opening a file:-
"r" - Read ---> (Default) Open file only in read mode and can not we do other mode operation later. and We can get error if the file does not exist at location.
"w" - Write ---> (Over-write) Open file in write mode only and Over-write the existing content i.e replace it entirely; if file is not present then it creates the file first.
"a" - Append ---> (add at the end) Opens a file for writing with appending content at the end of existing content; if file is not present, then it creates the file first.
"x" - Create ---> Creates the specified file, returns an error if the file exists
"+"  ----> using plus we can perform two operation later on (like reading and writting at same time. Ex: r+, w+, a+, )

In addition, we can specify if the file should be opened as binary or text mode-
"t" - Text ---> (Default value) to open a file in Text data.
"b" - Binary ----> To open a file in Binary data (e.g. images)
"rt"  ---> to combine two modes
"rb"  ---> to combine two modes


--------------------------------------------------------------------------------

#1.) Read a file :- We use .read() function to read a file once it opened using .open(). and .read() function returned all data in form of string. We can mention no of character to read only just pass the character number as argument to read() method.

Syntax :-
f = open("demo.txt",, "r") # we skip "r" coz it is default value for open() method.
data = f.read()  # to read the file
f.close() 

## Note : It is good programmer habbit to close the file once read or any FILE I/O operation has been done. If It is open then there might be some risk of file manupulation by someoneone else and it is not good practice to do once we doing any File I/O, close the file as soon as read, write, delete operation done


'''

#a)  read() - read whole text or entire content.
# f = open("G:\My Work - Mphasis Laptop\Python TUTORIAL\README.md", "r" )
# data = f.read() # To read it
# print(data)

# print(f.read(11)) # it will not work coz ahead of it we already read our entire content.

# f.close() # to close file once read operation done.

#b)  read(11) - read first 11 character from the file mentioned.
# f = open("G:\My Work - Mphasis Laptop\Python TUTORIAL\README.md", "r" )
# data = f.read(11)
# print(data)

# f.close()

#c)  () - reads one line at a time from the file content means this method returns one line at a time, so we can use it multiple times to read next line till end or depends.

# thus, By calling readline() two times, you can read the two first lines.
# f = open("G:\My Work - Mphasis Laptop\Python TUTORIAL\README.md", "r" )

# print(f.readline()) # Printing first line only
# print(f.readline()) # Printing the next line after first line..so on..

# f.close()

# Note : if we read complete content by using .read() and then followed by either .read(10) or .readline() then it wont read coz at first we read all data so no data left to read.





#2.) Write a File : - To write a file using write() method, you must first open it via either two modes -

# "a" - Append - (add to end of file) will append to the end of the file
# "w" - Write - (over write file) will overwrite any existing content.
# "x" - Create - (create file highlight) will create a file, returns an error if the file exists.

# Note : "a" and "w" can also create the file first like demo.text; if it not exist and then add the content.

# f = open("G:\My Work - Mphasis Laptop\Python TUTORIAL\Basics\demo.txt", "w")
# f.write("\nWe should Rock")
# f.close()


# f = open("G:\My Work - Mphasis Laptop\Python TUTORIAL\Basics\demo.txt", "a")
# f.write("\nWe should Rock 4")
# f.write("\nWe should Rock 5 ")
# f.write("\nWe should Rock 6")
# f.close()


# f = open("G:\My Work - Mphasis Laptop\Python TUTORIAL\Basics\demo.txt", "x")
# f.write("\nWe should Rock 4")
# f.write("\nWe should Rock 5 ")
# f.write("\nWe should Rock 6")
# f.close()


# Two Modes at a time (read and write) - r+, w+, a+

# f = open("G:\My Work - Mphasis Laptop\Python TUTORIAL\Basics\demo.txt", "a+")
# f.write("\nWe are Rowdyyy")
# print(f.read())
# f.close()





##3.) Using 'With' Statement to read and write a File :- We can use 'with' syntax to peform all File I/O with much easier than what we were doing before, here we do not have to worry about closing our file once opened, coz with statement takes care of closing it as our task ends.

# Syantax : 
# Opening a file as 'f' which acts like a stream then we can perform read or write - ( 'as' refer as alias)
with open("G:\My Work - Mphasis Laptop\Python TUTORIAL\Basics\demo.txt", "r") as f:
  print(f.read())

# Note : Here, we do not need to worry about closing the opened file, it handled by with statement. But If you are not using the with statement, you must write a close statement in order to close the file.

 
# with open("demo.txt") as f:
#   print(f.readline())  ##Read one line of the file.

# with open("demofile.txt") as f:
#   print(f.readline())
#   print(f.readline())  ##Read First two line of the file.



with open("G:\My Work - Mphasis Laptop\Python TUTORIAL\Basics\demo.txt", "w") as f:
  print(f.write("Wowwwwwwwwwwwww"))





## 4. Delete a File : - To Delete an existing file, Python doensot provide .delete() method, python uses 'os' module to delete a file using os's .remove() method -

# Syntax : -
# import os
# os.remove("<file_path_location>")

# import os
# os.remove("G:\My Work - Mphasis Laptop\Python TUTORIAL\Basics\demo1.txt")

# After Running above file get delete from your system.  

# Note : To delete an entire folder, use the os.rmdir("<folder_location_path>") method:
# Note: You can only remove empty folders.

# ----------------------------------------------------------------

# Let's PRactice : -

''' 1) Create a new file "practice.txt" using python and Add following data in it -
        Hi everyone
        we are learning File I/O
        using Python.
        I like programming in Python and Javascript.

'''

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using python.\nI like programming in python and Javascript.")


# 2. WAP that replaces all occurance of "Python" with "Java" in above file.


def replaceWords(word, newWord):
   
   with open("G:\My Work - Mphasis Laptop\Python TUTORIAL\practice.txt", "r") as f :
        content = f.read()

        newdata = content.replace(word, newWord)
 
        # print(newdata)

   with open("G:\My Work - Mphasis Laptop\Python TUTORIAL\practice.txt", "w") as f:
         f.write(newdata)     

  
replaceWords("python", "Java")


#3. WAP to search of the word "learning" is present in the file or not.

def search(word):
  with open("G:\My Work - Mphasis Laptop\Python TUTORIAL\practice.txt", "r") as f:
      data = f.read()

      if data.find(word) == -1 :
          print("Not Exist")
      else:
          print("Exist") 

      
      # if word in data:
      #     print("Exist")
      # else:
      #     print("Not Exist")   

search("Learning")
