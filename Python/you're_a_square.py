import math
def is_square(i):    
    if i<0: 
        return False
    if int(math.sqrt(i))**2 == i:
      return True
# fix me

print(is_square(4))