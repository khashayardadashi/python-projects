#import random library to generate custom numbers
import random
def probability (n):
    # n shows the number of times the program is executed
    outcomes=[]
    i=0
    for i in range(0,n+1):
        i=i+1
        #It produces a number between 0 and 1, which includes 0 and 1
        number=random.uniform(0,1)
        #Checking that the generated number is between [0,0.2] or not
        if(number>=0 and number<=0.2):
            outcomes.append(1)
        #Checking that the generated number is between (0.2,0.5] or not
        elif(number>0.2 and number<=0.5):
            outcomes.append(2)
        #Checking that the generated number is between (0.5,0.9] or not
        elif(number>0.5 and number<=0.9):
            outcomes.append(3)
        #Checking that the generated number is between (0.9,1] or not
        elif(number>0.9 and number<=1):
            outcomes.append(4)
    #Obtaining the probability of each interval as a percentage
    number1=(outcomes.count(1)/n)*100
    number2=(outcomes.count(2)/n)*100
    number3=(outcomes.count(3)/n)*100
    number4=(outcomes.count(4)/n)*100

    print(f'probability fo 1 : {number1}')
    print(f'probability fo 2 : {number2}')
    print(f'probability fo 3 : {number3}')
    print(f'probability fo 4 : {number4}')
    print(f'sum of possibilities : {number1 + number2 + number3 + number4}')

probability(1000000)



