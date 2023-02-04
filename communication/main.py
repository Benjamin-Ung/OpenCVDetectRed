from subprocess import Popen, PIPE
import subprocess

#C++ file must be compiled to run the file / use .exe file
def main():
    with Popen(["test.exe"], stdout=PIPE) as p:
        while True:
            line = p.stdout.readline()
            if not line: break
            print(line)
            print("This is not a block")    

main()

# with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
#     for line in p.stdout:
#         print(line, end='') # process line here

 # with Popen(["C++","test.cpp"], stdout = PIPE) as p:
    