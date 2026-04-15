
'''  Note : For Setup VSCode for taking Input and Ouput as Competitive Programming Interface :- 

# Step1 : Add Code Runner Extension and Python Extension
# Step2 : Create a input.txt file in the current directory for giving input to each code running, then open 'settings.json' file of vs code, then paste following there -

    {
    "code-runner.executorMap": {
        "python" : "cd $dir && python $fileName < input.txt > output.txt"
    },
    "code-runner.runInTerminal" : true
    }

Here, Whenever user clicks on the Runner Button, then it runs the current.py file with taking optional input from the input.txt file and gives the output in the output.txt file.

If you want output display only in terminal then remove '> output.txt' from json setting of vs code above.

Note : TO work code correcly with input.txt, then must keep input.txt file in the same folder along with main.py file.


# Advance Way using run_python.bat file creation -
Step1 : create a file run_python.bat in directory -
> C:\tools\run_python.bat

and add following code -


@echo off
cd /d "%~dp1"

if exist input.txt (
    python "%~1" < input.txt
) else (
    python "%~1"
)



Step2 : Add below in path of environment variable -
> C:\tools

Step3 : Either run directory from terminal -
> run_python.bat myscript.py


Or, paste into setting.json file as and Run from Code Runner Button -

  "code-runner.executorMap": {
    "python": "run_python.bat"
    }


'''

# Input() : Rememeber always, input() method always takes input values as string datatype.

# i) taking String Input(name) -
name = input()  # we get string datatype bydefault.
print(name, type(name))  # Prakash Verma <class 'str'>

# ii) Taking Integer as Input(age)
age = int(input())  # used type casting to convert input string into integer.
print(age, type(age))  # 5 <class 'int'>


# iii) Taking Float as Input(salary) -
salary = float(input())
print(salary, type(salary))

# iv) Taking Boolean value as Input (isAdmin)
isAdmin = bool(input())
print(isAdmin, type(isAdmin))


'''





'''
