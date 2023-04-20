def AFD(line,ansii):
    state=1
    for symbol in line:
        if symbol == 'k':
            if state == 9:
                state =10
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            else:
                state =1
                
        elif symbol =='a':
            if state == 8:
                state=9
            elif state == 11 or state==97 or state==100 or state==142:
                state=12
            elif state == 15 or state==143:
                state=16
            elif state == 21 or state==76 or state==93:
                state=94
            elif state == 29:
                state=30
            elif state == 56:
                state=57
            elif state == 124:
                state=125
            else:
                state=2
                
        elif symbol == 'b':
            if state == 35:
                state=36
            else:
                state=6
                
        elif symbol == 'c':
            if state == 96:
                state=97
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 99:
                state=100
            elif state == 141:
                state=142
            else:
                state=11
                
        elif symbol == 'd':
            if state == 87:
                state=88
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 115:
                state=116
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 105:
                state=106
            elif state == 122:
                state=123
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            else:
                state=27
                
        elif symbol == 'e':
            if state == 7:
                state=8
            elif state == 17:
                state=72
            elif state == 13:
                state=14
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 25:
                state=26
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 27:
                state= 28
            elif state == 37:
                state=38
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 45:
                state=46
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 48:
                state=49
            elif state == 50 or state==137 or state == 98 or state == 54 or state == 71 or state == 78 or state == 81:
                state=72
            elif state == 76:
                state=77
            elif state == 86:
                state=87
            elif state == 89:
                state=90
            elif state == 104:
                state=105
            elif state == 106:
                state=107
            elif state == 114:
                state=115
            elif state == 128:
                state=129
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 133:
                state=134
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            else:
                state=40
                
        elif symbol == 'f':
            if state == 23 or state==117 or state==112 or state == 96 or state == 63 or state == 74 or state == 84:
                state=66
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 28:
                state=29
            elif state == 91:
                state=92
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 107:
                state=108
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            else:
                state=52
                
        elif symbol == 'g':
            if state == 8 or state == 72:
                state = 73
            elif state == 69:
                state=70
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 84:
                state=85
            elif state == 112:
                state=113
            else:
                state=59

        elif symbol == 'h':
            if state==11 or state == 97 or state == 100:
                state=15
            elif state == 13 or state == 111 or state == 83 or state == 20 or state == 45 or state == 75:
                state=135
            elif state == 130 or state == 139:
                state=131
            elif state == 142:
                state=143
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            else:
                state=1
                
        elif symbol == 'x':
            if state == 40:
                state = 47
            else:
                state=1

        elif symbol == 'l':
            if state == 134 or state == 40 or state == 129 or state == 115 or state == 107 or state == 105 or state == 90 or state == 87 or state == 77 or state == 72 or state == 49 or state == 46 or state == 38 or state == 8 or state == 14 or state == 26 or state == 28:
                state = 44
            elif state == 108 or state==66 or state == 92 or state == 29 or state == 52:
                state = 55
            elif state == 31:
                state = 32
            elif state == 36:
                state = 37
            elif state == 121:
                state=124
            elif state == 127:
                state = 128
            elif state == 132:
                state = 133
            else:
                state=67
            
        elif symbol == 'i':
            if state == 13 or state==20 or state==45 or state==75 or state==83:
                state=84
            elif state == 22:
                state=23
            elif state == 73:
                state=74
            elif state == 95:
                state=96
            elif state == 110:
                state=117
            elif state == 111:
                state=112
            elif state == 121:
                state=122
            elif state == 126:
                state=127
            elif state == 131:
                state=132
            elif state == 139:
                state=140
            else:
                state=63
                
        elif symbol == 'm':
            if state == 42:
                state=43
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            else:
                state=1
                
        elif symbol == 'n':
            if state == 3 or state == 109 or state == 99 or state == 80 or state==42 or state == 35 or state == 25 or state == 31:
                state=110
            elif state == 8 or state ==134 or state == 115 or state == 107 or state == 105 or state == 90 or state == 87 or state == 77 or state == 72 or state == 49 or state == 46 or state == 40 or state == 38 or state == 14 or state == 26 or state == 28:
                state=41
            elif state == 23:
                state=24
            elif state == 18:
                state=19
            elif state == 50:
                state=51
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 56 or state == 68:
                state=69
            elif state == 63 or state == 140 or state == 132 or state == 127 or state == 122 or state==117 or state == 112 or state == 96 or state == 84 or state == 74:
                state=64
            elif state == 81:
                state=82
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 85:
                state=86
            elif state == 113:
                state=114
            elif state == 118:
                state=119
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            else:
                state=1
                
        elif symbol == 'r':
            if state == 6:
                state=7
            elif state == 16:
                state=17
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 21 or state == 93:
                state=98
            elif state == 36:
                state=7
            elif state == 49:
                state=50
            elif state == 53:
                state=54
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 76:
                state=98
            elif state == 77:
                state=78
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state ==136:
                state=137
            elif state == 80:
                state=81
            else:
                state=71
                
        elif symbol == 'p':
            if state ==  103:
                state=104
            else:
                state=1
                
        elif symbol == 'o':
            if state == 4:
                state=5
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 142 or state == 11 or state==97 or state == 100:
                state=18
            elif state == 123 or state == 106 or state == 27 or state == 88:
                state=34
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 108 or state == 92 or state == 29 or state == 52 or state == 66:
                state=53
            elif state == 124 or state == 67 or state == 32 or state == 37 or state == 44:
                state=68
            elif state == 55:
                state=56
            elif state == 113 or state == 59 or state ==85 or state==70 or state == 73:
                state=60
            elif state == 61:
                state=62
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 90:
                state=91
            elif state == 117:
                state=118
            elif state == 120:
                state=121
            elif state == 135:
                state=136
            else:
                state=71
                
        elif symbol == 's':
            if state == 12:
                state=13
            elif state == 19:
                state=20
            elif state == 44:
                state=45
            elif state == 74:
                state=75
            elif state == 110:
                state=111
            else:
                state=83
                
        elif symbol == 't':
            if state == 3 or state == 31:
                state=4
            elif state == 8 or state == 72:
                state=79
            elif state == 83 or state == 111 or state == 13 or state == 45:
                state=93
            elif state == 19:
                state=22
            elif state == 20:
                state=21
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 24 or state == 64:
                state=65
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 32:
                state=33
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 47:
                state=48
            elif state == 57:
                state=58
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 60:
                state=61
            elif state == 75:
                state=76
            elif state == 94:
                state=95
            elif state == 100:
                state=101
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 125:
                state=126
            elif state == 137:
                state=138
                tupla=ansii[state]
                tupla[1]=tupla[1]+1
            elif state == 140:
                state=141
            else:
                state=102
                
        elif symbol == 'u':
            if state == 2 or state == 125 or state == 94 or state == 9 or state == 12 or state == 16:
                state=3
            elif state == 24:
                state=25
            elif state == 30:
                state=31
            elif state==34:
                state=35
            elif state==41:
                state=42
            elif state == 79:
                state=80
            elif state == 98:
                state=99
            else:
                state=109
                
        elif symbol == 'v':
                state=120
                
        elif symbol == 'w':
            if state == 13 or state == 111 or state == 83 or state == 20 or state == 45 or state == 75:
                state=139
            else:
                state=130
                
        elif symbol == 'y':
            if state == 4 or state==141 or state == 138 or state == 126 or state == 102 or state == 101 or state == 95 or state == 93 or state == 79 or state == 76 or state == 65 or state == 61 or state == 58 or state == 48 or state == 21 or state == 22 or state == 33:
                state=103
            else:
                state=1
                
        elif symbol == 'z':
            if state == 84 or state == 112:
                state=89
            else:
                state=1
        else:
            state=1      
    return
    
def ClearAnsii(ansii):
    for qF in ansii:
        tupla=ansii[qF]
        tupla[1]=0
    return

def Output(out,ansii,lineNumber):
    out.write("\nIn line%d:\n"%(lineNumber))
    for qF in ansii:
        tupla=ansii[qF]
        if tupla[1]!=0:
            out.write(str(ansii[qF])+"\n")
    return

if __name__ == '__main__':
    file_name=input("Type file name: ")
    c_file=open(file_name,"r")
    ansii={
        #qF : (string,contador)
        5:["auto",0],
        10:["break",0],
        14:["case",0],
        17:["char",0],
        21:["const",0],
        26:["continue",0],
        33:["default",0],
        34:["do",0],
        38:["double",0],
        43:["enum",0],
        46:["else",0],
        51:["extend",0],
        54:["for",0],
        58:["float",0],
        62:["goto",0],
        65:["int",0],
        66:["if",0],
        70:["long",0],
        78:["register",0],
        82:["return",0],
        88:["signed",0],
        92:["sizeof",0],
        97:["static",0],
        101:["struct",0],
        108:["typedef",0],
        116:["unsigned",0],
        119:["union",0],
        123:["void",0],
        129:["volatile",0],
        134:["while",0],
        138:["short",0],
        143:["switch",0]
    }

    if c_file.mode == 'r':
        lines=c_file.readlines()
        lineNumber=1
        out=open("output.txt","w+")
        for line in lines:
            AFD(line,ansii)
            Output(out,ansii,lineNumber)
            ClearAnsii(ansii)
            lineNumber=lineNumber+1
        out.close()
        

