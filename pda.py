import random
import matplotlib.pyplot as plt
from tkinter import *
import turtle
from turtle import *
import time

def simulation(Input,State,Stack,Pinput,Pstate,Pstack):
    Pinput.write(Input, font=style)
    Pstack.write(Stack, font=style)
    Pstate.write(State, font=style)
    time.sleep(1)
    return

def getStackString(stack):
    stackString=''
    size=len(stack)
    for i in range(size):
        stackString = stackString + stack[size-i-1]
    return stackString

def randomString(size):
    string=''
    symbol='0'
    for i in range(random.randint(0,20)):
        string=string+symbol
    symbol='1'
    for i in range(random.randint(0,20)):
        string=string+symbol
    return string

def getInput(string,n):
    currentString=''
    for i in range(len(string)-n):
        currentString = currentString + string[i+n]
    return currentString

    
if __name__ == '__main__':
    option=int(input("1: Random string\n2: Type string\n"))    
    if option == 2:
        cad=input("Enter a string:")
    else:
        cad = randomString(random.randint(0,50))
    style = ('Courier', 30, 'italic')
    Pinput = Pen()
    Pstack = Pen()
    Pstate = Pen()
    Pinput.up()
    Pstack.up()
    Pstate.up()
    Pinput.goto(-600,200)
    Pstate.goto(-600,0)
    Pstack.goto(-600,-200)
    state = 'p'
    stack = ['Z']
    file = open("Descriptions.txt","w+")
    stackString = 'Z'
    n=1
    file.write("(%c,%s,%s) -> \n"%(state,cad,stackString))
    simulation(cad,state,stackString,Pinput,Pstate,Pstack)
    for symbol in cad:
        top = stack[len(stack)-1]
        if state == 'p':
            if symbol == '0':
                stack.append('X')
            else:
                if top == 'X':
                    state ='q'
                    stack.pop()
                else:
                    break
        else:
            if symbol == '1' and top == 'X':
                stack.pop()        
            else:
                break
        stackString = getStackString(stack)
        remainingInput = getInput(cad,n)
        Pinput.clear()
        Pstack.clear()
        Pstate.clear()
        file.write("(%c,%s,%s) -> \n"%(state,remainingInput,stackString))
        simulation(remainingInput,state,stackString,Pinput,Pstate,Pstack)
        n=n+1
    var=stack.pop()
    Pinput.clear()
    Pstack.clear()
    Pstate.clear()
    if var == 'Z':
        if len(cad) == n-1:
            file.write("(f,e,Z)")
            simulation("","f","Z",Pinput,Pstate,Pstack)
        else:
            remainingInput = getInput(cad,n-1)
            file.write("(f,%s,Z)"%remainingInput)
            simulation(remainingInput,"f","Z",Pinput,Pstate,Pstack)
    else:
        stackString = getStackString(stack)
        if len(cad) != n-1:
            remainingInput = getInput(cad,n-1)
            file.write("(f,%s,%s)"%(remainingInput,stackString))
            simulation(remainingInput,"f",stackString,Pinput,Pstate,Pstack)
        else:
            file.write("(f,e,X%s)"%stackString)
            simulation("","q","X"+stackString,Pinput,Pstate,Pstack)
    file.close()
