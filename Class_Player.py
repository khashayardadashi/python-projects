from random import choice
#CLASSES
class Human:
    def __init__(self,name):
        self.name=name
class Player(Human):
    l=[]
    def __init__(self, name):
        super().__init__(name)
        self.l.append(self.name)

#OBJECTS
a1=Player('1')
a2=Player('2')
a3=Player('3')
a4=Player('4')
a5=Player('5')
a6=Player('6')
a7=Player('7')
a8=Player('8')
a9=Player('9')
a10=Player('10')
a11=Player('11')
a12=Player('12')
a13=Player('13')
a14=Player('14')
a15=Player('15')
a16=Player('16')
a17=Player('17')
a18=Player('18')
a19=Player('19')
a20=Player('20')
a21=Player('21')
a22=Player('22')

#SEPRATE OBJECTS INTO TWO GROUPS
a=[]
b=[]
c=len(Player.l)//2
while len(a)!=c:
    a1=choice(Player.l)
    a.append(a1)
    Player.l.remove(a1)
print('TaemA:',end='')
for i in a:
    print(i,end=',')
print()
while len(b)!=c:
    b1=choice(Player.l)
    b.append(b1)
    Player.l.remove(b1)
print('TaemB:',end='')
for i in b:
    print(i,end=',')
