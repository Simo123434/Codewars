def is_valid_walk(walk):
    #take input array and if ends up in original position
    x = 0
    y = 0
    for i in range(len(walk)):
        if walk[i] == 'n':
            y+=1
        elif walk[i] == 's':
            y-=1
        elif walk[i] == 'e':
            x+=1
        elif walk[i] == 'w':
            x-=1            
            
    if (len(walk) == 10) and (x == 0 and y == 0):
        return True

    else:
        return False
        
        
is_valid_walk(['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 'w'])