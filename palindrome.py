import random

if __name__ == '__main__':
    productionRules = {
        0 : '',
        1 : '0',
        2 : '1',
        3 : '0P0',
        4 : '1P1'
    }
    
    option=int(input("1: Random size\n2: Type size\n"))
    file=open("derivation.txt","w+")
    if option == 2:
        size=int(input("Type size:"))
    else:
        size=random.randint(1,100)
        
    file.write("Basis:\nP =>* P;\n")
    string = productionRules[random.randint(3,4)]
    file.write("Induction:\nP =>* %s; \n"%(string))
    tam=int(size/2)
    for i in range(tam):
        string=string.replace("P",productionRules[random.randint(3,4)])
        file.write("P =>* %s; \n"%(string))
    string=string.replace('P',productionRules[random.randint(0,2)])
    file.write("P =>* %s; \n\n"%(string))
    file.close()
