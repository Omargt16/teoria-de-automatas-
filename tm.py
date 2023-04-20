#Turing machine
#page 346 introduction to automata theory...
import random

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

def randomString(size):
    string=''
    symbol='0'
    for i in range(random.randint(0,20)):
        string=string+symbol
    symbol='1'
    for i in range(random.randint(0,20)):
        string=string+symbol
    string= 'B'+string+'B'
    return string

def addItem(string,index,item):
    newString=''
    left=string[:index]
    right=string[index+1:]
    newString=left+item+right
    return newString

def moveLeft(state,string,i):
    while i > 0:
        i=i-1
        if state == 2:
            if string[i] == '0':
                file.write('\n'+addItem(listToString(string),i,'(q_2)0')+' |-')
                string[i]='0'
                state=2
            elif string[i] == 'Y':
                file.write('\n'+addItem(listToString(string),i,'(q_2)Y')+' |-')
                string[i]='Y'
                state=2
            else:
                break
    return i

if __name__ == '__main__':

    option=int(input("1: Type string\n2:Random string:\n"))
    if option == 1:
        cad=input("Type string: ")
        cad='B'+cad+'B'
    else:
        cad=randomString(random.randint(1,50))

    state=0
    string=list(cad)
    i=0
    file = open("Descriptions.txt","w")
    file.write("Turing Machines Descriptions\n")

    while i < len(string)-1:
        if state == 0:
            if string[i+1] == '0':
                file.write('\n'+addItem(listToString(string),i+1,'(q_0)0')+' |- ')
                state=1
                string[i+1]='X'
            elif string[i+1] == 'Y':
                file.write('\n'+addItem(listToString(string),i+1,'(q_0)Y')+' |- ')
                state=3
                string[i+1]='Y'

        elif state == 1:
            if string[i+1] == '0':
                file.write('\n'+addItem(listToString(string),i+1,'(q_1)0')+' |- ')
                state=1
                string[i+1]='0'
            elif string[i+1] == '1':
                file.write('\n'+addItem(listToString(string),i+1,'(q_1)1')+' |- ')
                state=2
                string[i+1]='Y'
                i=moveLeft(state,string,i+1)
                i=i-2
            elif string[i+1] == 'Y':
                file.write('\n'+addItem(listToString(string),i+1,'(q_1)Y')+' |- ')
                state=1
                string[i+1]='Y'

        elif state == 2:    
            if string[i+1] == 'X':
                file.write('\n'+addItem(listToString(string),i+1,'(q_2)X')+' |- ')
                state=0
                string[i+1]='X'
                
        elif state == 3:
            if string[i+1] == 'Y':
                file.write('\n'+addItem(listToString(string),i+1,'(q_3)Y')+' |- ')
                state=3
                string[i+1]='Y'
            elif string[i+1] == 'B':
                file.write('\n'+addItem(listToString(string),i+1,'(q_3)B')+' |- ')
                state=4
                string[i+1]='B'
                file.write('\n'+addItem(listToString(string),i+1,'B(q_4)')+'\n')
            else:
                break
        i=i+1
    file.close()
    if state == 4:
        print("Accepted!")
    else:
        print("Rejected!")

            
            
