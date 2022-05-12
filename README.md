# AcloudguruPython3
Python 3 Scripting

print("Hello, World!")

or

Executable from anywhere (in our $PATH).
Executable without explicitly using the python3.6 CLI.
Thankfully, we can set the process to interpret our scripts by setting a shebang at
the top of the file: and can execute without using python3.6 CLI
hello.py

Setting shebang
#!/usr/bin/env python3.6
print("Hello, World")

to make this happen we have to provide execute permissions to hellp.py 

chmod u+x hello.py
