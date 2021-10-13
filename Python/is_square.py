import math

def is_square(n):
    yes = 0
    if len(n) == 0:
        return None
    for i in n: 
        if int(math.sqrt(i))**2 == i:
            yes += 1        
    if yes == len(n):
        print('square')
        return True
    else:
        print('not square')
        return False
        

        
        