import numpy as np

def isOverlap(line1,line2):

    ''' This function check if two lines are overlapped
        Input: 2 tuples containing the coordinates
        Output: True -> Are overlapped
        False -> Not overlaped
    '''
    
    #Get all coordinates
    lines = [round(coord,1) for coord in line1+line2]

    x1,x2,x3,x4 = lines

    #Check if direction of coordinates    
    s1 = 0.1 if x2 >= x1 else -0.1
    s2 = 0.1 if x4 >= x3 else -0.1

    #Create space
    space1 = {round(x,1) for x in np.arange(x1,x2+s1,s1)}
    space2 = {round(x,1) for x in np.arange(x3,x4+s2,s2)}

    #Returns True if was found some intersection between lines, or False
    return bool(space1.intersection(space2))