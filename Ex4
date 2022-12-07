def chess():
    KnightH=input('please enter horizontal for Knight(a,b,c,d,e,f,g,h):')
    list1=['a','b','c','d','e','f','g','h']
    list2=['A','B','C','D','E','F','G','H']
    list3=['1','2','3','4','5','6','7','8']
    alphabet={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
    z1=[[1,2],[-1,2],[2,1],[2,-1],[-2,-1],[-1,-2],[1,-2],[-2,1]]
    z2=[[1,1],[1,-1],[-1,-1],[-1,1]]
    if len(KnightH)>1 or (KnightH.isnumeric()==True):
        return('Horizontal input for Knight is not a letter')
    elif (KnightH not in list1) and (KnightH not in list2):
        return('horizontal input for Knight is not a proper lette')
    KnightV=input('please enter vertical for Knight(1,2,3,4,5,6,7,8):')
    if (KnightV.isnumeric()==True) and  (KnightV not in list3):
        return('Vertical input for Knight is not a proper number')
    elif KnightV not in (list3):
        return('Vertical input for Knight is not a number')
    x=[]
    y=[]
    H1=alphabet[KnightH]
    V1=int(KnightV)
    for i in range (0,8):
        H1 +=z1[i][0]
        V1 +=z1[i][1]
        if H1 in range (0,9):
            x.append(H1)
        if V1 in range (0,9):
            y.append(V1)
        H1 -= z1[i][0]
        V1 -= z1[i][1]
    while len(x)!=len(y):
        if len(x)>len(y):
            x.pop()
        elif len(y)>len(x):
            y.pop()
    BishopH=input('please enter horizontal for Bishop(a,b,c,d,e,f,g,h):')
    if len(BishopH)>1:
        return('Horizontal input for Bishop is not a letter')
    elif(BishopH not in list1) and (BishopH not in list2):
        return('horizontal input for Bishop is not a proper letter')
    BishopV=input('please enter vertical for Bishop(1,2,3,4,5,6,7,8):')
    if (BishopV.isnumeric()==True) and  ( BishopV not in list3):
        return('Vertical input for Bishop is not a proper number')
    elif BishopV not in (list3):
        return('Vertical input for Bishop is not a number')
    a=[]
    b=[]
    V2=int(BishopV)
    H2=alphabet[BishopH]
    for j in range (0,4):
        H2+=z2[j][0]
        V2+=z2[j][1]
        if H2 in range (0,9):
            a.append(H2)
        if V2 in range (0,9):
            b.append(V2)
        H2 -= z2[j][0]
        V2 -= z2[j][1]
    while len(a)!=len(b):
        if len(a)>len(b):
            a.pop()
        elif len(b)>len(a):
            b.pop()
    if (KnightH==BishopH) and (KnightV==BishopV):
        return 'They can not be in the same square'
    if (V2 in y) and (alphabet[BishopH] in x):
        return 'Knight can attack Bishop'
    elif (V1 in b) and (alphabet[KnightH] in a):
        return 'Bishop can attack Knight'
    elif KnightV==BishopV :
        return 'Niether of them can attack each other'

print(chess())
