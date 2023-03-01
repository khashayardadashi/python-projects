#The distance between two points
from math import sqrt
A=input('')
B=input('')
A=A.split(' ')
B=B.split(' ')
l=[int(j) for j in A]
l1=[int(i) for i in B]
a=((l[0]-l1[0])**2)+((l[1]-l1[1])**2)
b=sqrt(a)
c=float('{:.2f}'.format(b))
print(int(c))

#print(firstname,lastname,age)
input=input('')
A=input.split(' ')
B=1401-int(A[2])+1
print(f'Dear {A[0].capitalize()} {A[1].capitalize()},your age is {B}')

#BMI
name=input('')
w_h=input('')
l=w_h.split(' ')
a=float(l[0])
b=float(l[1])
b=b/100
BMI=a/(b*b)
BMI=float('{:.3f}'.format(BMI))
print(f'{name.upper()} your BMI is:{BMI}')
