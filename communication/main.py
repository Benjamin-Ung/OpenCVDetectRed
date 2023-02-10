from subprocess import Popen, PIPE
import subprocess

#https://stackoverflow.com/questions/6906922/threading-subprocesses-in-python
#https://stackoverflow.com/questions/42553481/check-on-the-stdout-of-a-running-subprocess-in-python

#C++ file must be compiled to run the file / use .exe file
def main():
    with Popen(["test.exe"],stdout = PIPE) as p:
        while True:
            line = p.stdout.readline()
            if not line: break
            print("This is not blocking") 
            print(line)
            
    print("process is done in the background")

main()

# with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
#     for line in p.stdout:
#         print(line, end='') # process line here

 # with Popen(["C++","test.cpp"], stdout = PIPE) as p:
    