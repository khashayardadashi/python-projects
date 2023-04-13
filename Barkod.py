barkod=input()
a1=[]
a2=[]
a3=[]
d1=[]
d2=[]
for i in barkod:
    if i.isnumeric() and i=='0':
        a1.append(i)

if a1.count('0')==8:
    print('invalid barkod')

for i in barkod:
    if i.isnumeric()==True:
        break
    else:
        a2.append(i)

if len(a2)==1 or len(a2)==2:
    pass
else:
    print('invalid barkod')

for i in range(1,4):
    if barkod[-i].isnumeric()==True:
        break
    else:
        d1.append(barkod[-i])
def shomaresh(x):
    if len(x)==1:
        return '\'no replacment\''
    elif len(x)==2:
        return '\'replacment with payment\''
    elif len(x)==3:
        return '\'replacment without payment\''
    

for i in barkod:
    if i.isdigit()==True:
        d2.append(i)


numberchap=d2[-4]+d2[-3]
month=int(d2[-2]+d2[-1])
year=int(d2[0]+d2[1])

if  int(numberchap)%15==0:
    month=month+3
elif int(numberchap)%3==0 and int(numberchap) %5!=0:
    month=month+1

        
    


if year+(month/12)>23:
    print(f'The Gaurantee is valid for {(month%12)} month and Replacment Status is {shomaresh(d1)}')
elif year+(month/12) <= 23:
    print(f'No More Gaurantee and Replacment Status is {shomaresh(d1)}')
