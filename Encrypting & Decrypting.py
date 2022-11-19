import os
def writting(_file_,mode):
    with open(_file_,mode)as f:
        while True:
            new=""
            a=input("Enter >>>>>")
            for i in a:
                b=ord(i)+3
                new=new+chr(b)
            print(new,file=f)
            if "n" in input("Enter more line[yes or no]: "):
                break


def readfile(_file_,mode):
    with open(_file_,mode)as f:
        q=f.readlines()
    l=[]
    for a in q:
        a.strip("\n")
        new=""
        for i in a:
            b=ord(i)-3
            new=new+chr(b)
        l.append(new[:-1])
    return l
    

print("Hello user ...")
cwfile=input("Enter the file (.txt) to work on: ")
cwfile=cwfile+".txt"
print("""
write or rewrite      -w
add lines             -a
read                  -r
""")
work = input("What you want to do (#Case Sensative): ")
if work == "w":
    writting(cwfile,work)
    print("Task completed")
elif work == "a":
    writting(cwfile,work)
    print("Task completed")
elif work=="r":
    print()
    for i in readfile(cwfile,work):
        print(i)
else:
    print("No such operation can be performed!")
os.system("Pause")
