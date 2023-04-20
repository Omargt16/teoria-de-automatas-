import random

def addItem(string,index,item):
    newString=''
    left=string[:index]
    right=string[index+1:]
    newString=left+item+right
    return newString

def noBrackets(string):
    string=string.replace("(","")
    string=string.replace(")","")
    return string

def writeCode(string):
    file=open("code.py","w+")
    file.write("#%s\n\n"%noBrackets(string))
    level=-1
    for symbol in string:   
        if symbol == '(':
            level=level+1    
        elif symbol == ')':
            level=level-1
        elif symbol == 'i':
            indent='    '*level
            file.write("%sif "%indent)
        elif symbol == 'C':
            file.write("C:\n")
        elif symbol == 'S':
            indent='    '*(level+1)
            file.write("%s#statement\n"%indent)
        elif symbol == 'e':
            indent='    '*level
            file.write("%selse:\n"%indent)
    return

if __name__ == '__main__':
    string="(iCtSA)"
    num=int(input("1: Type number\n2: Random\n"))
    if num == 1:
        noIf=int(input("Number: "))
    else:
        noIf=random.randint(1,100)
    countIf=0
    indexAux=0
    index=0
    
    while countIf < noIf:
        if string[index] == 'S':
            countIf=countIf+1
            indexAux=index+7
            string=addItem(string,index,"(iCtSA)")
            while indexAux < len(string):
                if string[indexAux] == 'S':
                    countIf=countIf+1
                    if countIf < noIf:
                        break
                    string=addItem(string,indexAux,"(iCtSA)")
                    indexAux=indexAux+7
                elif string[indexAux] == 'A':
                    if random.randint(0,1) == 0:
                        string=addItem(string,indexAux,"")
                        indexAux=indexAux-1
                    else:
                        string=addItem(string,indexAux,"eS")
                        indexAux=indexAux+1
                indexAux=indexAux+1
        index=index+1
    if random.randint(0,1) == 0:
        string=string.replace("A","")
    else:
        string=string.replace("A","eS")
    writeCode(string)

