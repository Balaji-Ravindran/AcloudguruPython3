# AcloudguruPython3
Python 3 Scripting

print("Hello, World!")

or

Setting shebang
#!/usr/bin/env python3.6
print("Hello, World")

Executable from anywhere (in our $PATH).
Executable without explicitly using the python3.6 CLI.
We can set the process to interpret our scripts by setting a shebang at
the top of the file: and can execute without using python3.6 CLI

$ helloworld.py

To make this happen we have to provide execute permissions to helloworld.py 

chmod u+x helloworld.py


###### Reading User Input #######

age - Python script

In Python, we use input() function to take input from the user. Whatever you enter as input, the input function converts it into a string. If you enter an integer value still input() function convert it into a string

By default input() function takes the user’s input in a string. So, to take the input in the form of int you need to use int() along with the input function.
Ex: num = int(input("Enter a number:"))

float input along with the input function.
num =float(input("Enter number "))

list input along with the input function
li =list(input("Enter number "))

take tuple input along with the input function.
num =tuple(input("Enter number "))


