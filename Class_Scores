from statistics import mean
class Scores:
    '''This class get list and excute some methodes on it'''
    def __init__(self,list):
        self.l=list
    def __str__(self):
        print(f'<class \'Scores'\>')
    def __repr__(self):
        print(f'{self.__class__.__name__}')
    @property
    def first_grade(self):
        a1=self.l.pop(0)
        print(a1)
    @property
    def end_grade(self):
        a=self.l.pop()
        print(a)
    @property
    def average(self):
        t=0
        for i in self.l:
            t+=i
        t1=t/len(self.l)
        print(t1)
    @property
    def top3(self):
        n=0
        ll=[]
        while n!=3:
            a2=max(self.l)
            ll.append(a2)
            self.l.remove(a2)
            n+=1
        for i in ll:
            print(i)
