'''
# Way1 :- Create two input.txt and output.txt file and paste these code in every main.py code where we want to run -

  import sys
  sys.stdin = open('CodeRunnerSetup\input.txt', 'r')
  sys.stdout = open('CodeRunnerSetup\output.txt', 'w')


# Way2(using Now) : - Open VS Code settings.json, then paste following -

{
  "code-runner.executorMap": {
    "python": "cd $dir && python $fileName < input.txt > output.txt"
  },
  "code-runner.runInTerminal": true
}

Whenever user clicks on the Runner Button, then it runs the current.py file with taking optional input from the input.txt file and gives the output in the output.txt file.

Note : TO work code correcly with input.txt, then must keep input.txt file in the same folder along with main.py file.
Note : If you want output display only in terminal then remove '> output.txt' from json setting of vs code above.


# Way3 : Manually Running Current COde in terminal with taking input from input.txt and throwing the output in output.txt file -

> python current_file.py < input.txt > output.txt


'''


# taking input first line as 'user name' -

name = input()
print("My name is : ", name) 

print("Hello World")
print("Hello World 2")
print("Hello World 3") 


