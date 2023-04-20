import turtle 
from turtle import *
import time
import random

STRING_SIZE=10
Q0_P1=1
QF_P1=9
Q0_P2=3
QF_P2=7
MOVEMENT_TIME=2

#Create a superVector wiht all possible paths
def AFN(string,stateTable,q0):
    #q0 = Initial state string = input
    #CREATE VECTOR
    size=len(string)+1
    vector=[0]*size
    vector[0]=q0
    #We use it to add or insert new vectors in supervector
    vector_copy=[0]*size
    #We use it to know which are possible states of another state
    possibleStates=[]
    #Supervector
    superVector=[[]]
    superVector[0]=vector
    #We start by going through the vector contained in supervector
    vector_size=size-1
    for i in range(vector_size):#Enter to each number of vector
        superVector_index=0#Super vector index indicates the next possible state 
        while(superVector_index<=len(superVector)-1):#Chech every possible state ultil there's no more vectors 
            possibleStates=stateTable[(superVector[superVector_index][i],string[i])]#Get possible states per number in vector
            PossibleStatesSize=len(possibleStates)#get size of array
            superVector[superVector_index][i+1]=possibleStates[0]#First element in possible states is set in next vector position each time
            #make a copy
            copy(vector_copy,superVector[superVector_index])
            for k in range(PossibleStatesSize-1):#check the number of possible States
                vector_copy[i+1]=possibleStates[k+1]#Modify the vector copy by changing original number to possible state number
                #Make an auxiliar copy for avoiding problems
                auxiliar=[0]*size
                copy(auxiliar,vector_copy)
                if superVector_index==(len(superVector)-1): #There's no right adjacent vector, so we can just append the modified copy of first vector    
                    superVector.append(auxiliar)#add modify vector to supervector
                else: #We insert, so right adjacent vectors move
                    superVector.insert(superVector_index+1,auxiliar)
                superVector_index=superVector_index+1
            superVector_index=superVector_index+1
    return superVector

#Copy
def copy(copy,originalVector):
    for i in range(len(originalVector)):
        copy[i]=originalVector[i]
    return

#Create two files: one contains all possible vectors and the second contains just accepted vectors
#return a list with accepted vectors
def makeFiles(superVector,qF,allPaths_name,acceptedPaths_name):
    allPaths=open(allPaths_name,"w+")
    acceptedPaths=open(acceptedPaths_name,"w+")
    acceptedSuperVector=[]
    finalPos=len(superVector[0])-1
    for vector in superVector:
        allPaths.write(str(vector))
        allPaths.write('\n')
        if vector[finalPos]==qF:
            acceptedSuperVector.append(vector)
            acceptedPaths.write(str(vector))
            acceptedPaths.write('\n')
    acceptedPaths.close()
    allPaths.close()
    return acceptedSuperVector

#Draw the chessboard
def DrawChessboard():
    chessboard = turtle.Turtle()
    chessboard.speed(0) #Fastest speed
    coordinates=dict() #Coordinates record for moves
    a = 0 #for controlling alternate colors in a row
    b = 0 #for controlling alternate colors in a column
    x = 0
    y = 0
    cont = 9
    p = Pen()
    p.color('white','white')
    #for loop will run 3 times as there are 3 rows in the chessboard
    for i in range(3): 
        if(b == 0):
            a=1
        else:
            a=0
        #for loop will run 3 times as there are 3 colums in the chessboard
        for j in range(3): 
            x=j*100*(-1)
            y=i*100
            chessboard.penup()
            chessboard.goto(x,y)
            chessboard.pendown()
            if(a==0):
                chessboard.fillcolor('red')
                a=1
            else:
                chessboard.fillcolor('black')
                a=0
            #fill    
            chessboard.begin_fill()
            for k in range(4):
                chessboard.forward(100)
                chessboard.right(90)
            chessboard.end_fill()
            #Write number
            p.penup()
            p.goto(x+50,y-65)
            coordinates[cont]=(x+50,y-65)
            p.pendown()
            p.write(cont,False,'center',font=('Candara',20,'bold'))
            cont=cont-1
        if(b==0):
            b=1
        else:
            b=0
    p.penup()
    p.goto(x,y) #Goto 1 square
    return coordinates#It's a dictionary with the coordinates of each square of the chessboard 

def Move(posicion,x_y):
    posicion.goto(x_y)
    time.sleep(MOVEMENT_TIME)
    return

#Search for alternative paths
def Search(acceptedSuperVectors,MoveX,Move,VectorX,Vector,numX,num):
    found = False
    numVectors=len(acceptedSuperVectors[MoveX])
    actualPosition=acceptedSuperVectors[MoveX][VectorX][numX]
    VectorX=0
    while found == False and VectorX<numVectors:
        if acceptedSuperVectors[MoveX][VectorX][numX+1]!=acceptedSuperVectors[Move][Vector][num] and actualPosition==acceptedSuperVectors[MoveX][VectorX][numX]:
            found=True
        VectorX=VectorX+1
    return found,VectorX

#Show moves in chessboard
def ChessMoves(acceptedSuperVectors,coordinates,initialStates):
    size=len(acceptedSuperVectors)
    pos_player1 = Pen()
    pos_player1.color('blue','blue') #Choose your favorite color
    pos_player1.penup()#Don't write
    if size == 1:#1_player
        for i in range(3):#Simulate moves
            pos_player1.goto(coordinates[initialStates[0]]) #Goto to initial state in chessboard
            time.sleep(2) #Initial states
            choose=random.randint(0,len(acceptedSuperVectors[0])-1)#choose one move vector
            for j in range(len(acceptedSuperVectors[0][0])):
                Move(pos_player1,coordinates[acceptedSuperVectors[0][choose][j]])
            time.sleep(MOVEMENT_TIME) #Final state
    else:#2 players
        pos_player2 = Pen()
        pos_player2.color('white','white') #Choose your favorite color
        pos_player2.penup()#Don't write
        #Random turn 
        firstMove=random.randint(0,1)
        if firstMove == 0:
            secondMove=1
        else:
            secondMove=0
        pos_player1.goto(coordinates[initialStates[firstMove]]) #Goto to initial state in chessboard
        pos_player2.goto(coordinates[initialStates[secondMove]]) #Goto to initial state in chessboard
        time.sleep(2) #Wait 1 second
        Vector_n1=0 #We use it to search candidate paths for player 1
        Vector_n2=0 #We use it to search candidate paths for player 2
        vectorSize=len(acceptedSuperVectors[0][0])
        num=0
        num_2=0
        while num<vectorSize-1 and num_2<vectorSize-1:
            if acceptedSuperVectors[firstMove][Vector_n1][num+1] != acceptedSuperVectors[secondMove][Vector_n2][num_2]: 
                Move(pos_player1,coordinates[acceptedSuperVectors[firstMove][Vector_n1][num+1]])
                print("MOVE PLAYER 1")
                num=num+1
            else:
                auxVector_n1=Vector_n1
                print("Searching for alternative paths for PLAYER 1")
                found_1,Vector_n1= Search(acceptedSuperVectors,firstMove,secondMove,Vector_n1,Vector_n2,num,num_2)
                if found_1 == True:
                    Move(pos_player1,coordinates[acceptedSuperVectors[firstMove][Vector_n1][num+1]])
                    print("MOVE PLAYER 1")
                    num=num+1
                else:
                    Vector_n1=auxVector_n1

            if acceptedSuperVectors[firstMove][Vector_n1][num] != acceptedSuperVectors[secondMove][Vector_n2][num_2+1]:
                Move(pos_player2,coordinates[acceptedSuperVectors[secondMove][Vector_n2][num_2+1]])
                print("MOVE PLAYER 2")
                num_2=num_2+1
            else:
                auxVector_n2=Vector_n2
                print("Searching for alternative paths for PLAYER 2")
                found_2,Vector_n2= Search(acceptedSuperVectors,secondMove,firstMove,Vector_n2,Vector_n1,num_2,num)    
                if found_2 == True:
                    Move(pos_player2,coordinates[acceptedSuperVectors[secondMove][Vector_n2][num_2+1]])
                    print("MOVE PLAYER 2")
                    num_2=num_2+1
                else:
                    Vector_n2=auxVector_n2   
    return

#"""
#Deterministic Finite Automaton created from Non-deterministic finite automaton.
#Accept or reject string
def AFD(string):
    state='A'
    for symbol in string:
        #state A 
        if state=='A':
            if symbol=='r':
                state='B'
            else:
                state='C'
        #state B
        elif state=='B':
            if symbol=='r':
                state='D'
            else:
                state='E'
        #state C
        elif state=='C':
            if symbol=='r':
                state='D'
            else:
                state='F'
        #states D E and G
        elif state=='D' or state=='E' or state=='G':
            if symbol=='r':
                state='D'
            else:
                state='G'
        #state F
        elif state=='F': 
            if symbol=='r':
                state='D'
            else:
                state='C'
    #Is it a final state?
    if(state=='F' or state=='G'):
        return True
    else:
        return False

    
def createString(size):
    string=''
    for i in range(size):
        b=random.randint(0,1)
        if b==0:
            symbol='b'
        else:
            symbol='r'
        string=string+symbol
    return string

#"""
#MAIN
if __name__ == '__main__':
    #State table of AFN
    stateTable={
        (1,"r"):[2,4],
        (1,"b"):[5],
        (2,"r"):[4,6],
        (2,"b"):[1,3,5],
        (3,"r"):[2,6],
        (3,"b"):[5],
        (4,"r"):[2,8],
        (4,"b"):[1,5,7],
        (5,"r"):[2,4,6,8],
        (5,"b"):[1,3,7,9],
        (6,"r"):[2,8],
        (6,"b"):[3,5,9],
        (7,"r"):[4,8],
        (7,"b"):[5],
        (8,"r"):[4,6],
        (8,"b"):[5,7,9],
        (9,"r"):[6,8],
        (9,"b"):[5],
    }
    #Input
    c=input("Enter the number of players:\n")
    while(c!='1' and c!='2'):
        c=input("Enter the number of players:\n")
    nPlayers=(int)(c)

    if nPlayers == 1:
        option=input("Enter 1 to type string or 2 for a random string:\n")
        while(option!='1' and option!='2'):
            option=input("Enter 1 to type string or 2 for a random string:\n")
        if(option=='1'):
            string1=input("Type string:\n")
        else:
            size=random.randint(3,STRING_SIZE)
            string1=createString(size)
        print("String: %s"%(string1))
        string2=''
        string3=''
    else:
        option=input("Enter 1 to type string or 2 for a random string:\n")
        while(option!='1' and option!='2'):
            option=input("Enter 1 to type string or 2 for a random string:\n")
        if(option=='1'):
            string2=input("Type string 1:\n")
            string3=input("Type string 2:\n")
        else:
            size=random.randint(3,STRING_SIZE)
            string2=createString(size)
            string3=createString(size)
        print("First string: %s"%(string2))
        print("Second string: %s"%(string3))
        string1=''
    """
    OBSERVATIONS:
        *If the string has length n where first n-1 symbols are "r" and n symbol is "b", then there are 2^(n-1) possible paths
        *If the string has length n where first n-1 symbols are "b" and n symbol is "r", then there're not possible paths
        *Let have a string with lenght n where all symbols are "b":
            *If b is a pair number, then there are not possible paths
            *If b is an odd number, then there are possible paths
    """
    #Check and simulate string in chessboard
    if(AFD(string1) or (AFD(string2) and AFD(string3))):
        print("Accepted!")
        if nPlayers == 2:
            superVector_1=AFN(string2,stateTable,Q0_P1)
            superVector_2=AFN(string3,stateTable,Q0_P2)
            acceptedSuperVector_1=makeFiles(superVector_1,QF_P1,"allPaths1.txt","acceptedPaths1.txt")#Make files and get accepted paths
            acceptedSuperVector_2=makeFiles(superVector_2,QF_P2,"allPaths2.txt","acceptedPaths2.txt")#Make files and get accepted paths
            acceptedSuperVectors=[]
            acceptedSuperVectors.append(acceptedSuperVector_1)
            acceptedSuperVectors.append(acceptedSuperVector_2)
            print("Number of accepted paths of player 1:%d\nNumber of accepted paths of player 2:%d"%(len(acceptedSuperVector_1), len(acceptedSuperVector_2)))
            coordinates=DrawChessboard()#Draw chessboard and get a dictionary with coordinates of numbers
            ChessMoves(acceptedSuperVectors,coordinates,[Q0_P1,Q0_P2])#Simulate the moves
        else:
            superVector_1=AFN(string1,stateTable,Q0_P1)#All posible paths
            acceptedSuperVector_1=makeFiles(superVector_1,QF_P1,"allPaths1.txt","acceptedPaths1.txt")#Make files and get accepted paths
            print("Number of accepted paths: %d"%(len(acceptedSuperVector_1)))
            coordinates=DrawChessboard()#Draw chessboard and get a dictionary with coordinates of numbers
            ChessMoves([acceptedSuperVector_1],coordinates,[Q0_P1])#Simulate the moves
    else:
        print("No possible path!")


