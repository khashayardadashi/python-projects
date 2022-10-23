def EX1_5(person_age):
    if person_age<=1 :
        return(f'he or she is an infant')
    elif person_age>1 and person_age<13:
        return(f'he or she is a child')
    elif person_age>=13 and person_age<20:
        return(f'he or she is a teenage')
    elif person_age>=20:
        return(f'he or she is an adualt')
