import random
SIZE=100000

if __name__ == '__main__':
    strings=open("strings.txt","w+")
    selection=open("states.txt","w+")
    for i in range(10):
        strings.write("#%d: "%(i+1))
        selection.write("#%d\n"%(i+1))
        #For *
        kleene=random.randint(0,100)
        if kleene >= 10:
            selection.write("(0+10)* != e\n")
            #For (0+10)*
            union=random.randint(0,1)
            #Copies of 0
            if union == 0:
                selection.write("0*\n")
                copies=random.randint(1,SIZE)
                for copy in range(int(copies)):
                    strings.write("0")
            #Copies of 1
            else:
                selection.write("(10)*\n")
                copies=random.randint(1,SIZE)/2
                for copy in range(int(copies)):
                    strings.write("10")
        else:
            selection.write("(0+10)* = e\n")

        if random.randint(0,1) == 1:
            selection.write("(e+1) = 1\n")
            strings.write("1")
        else:
            selection.write("(e+1) = e\n")
        selection.write("\n")
        strings.write("\n")
    strings.close()
    selection.close()
