import numpy as np
from random import *
from datetime import datetime as dtt

# seed random number generator
seed(dtt.now())

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



def overlap_test(start,stop,nloop):

    x,_tmp = [],[]

    if isinstance(start,int) & isinstance(stop,int):

            for _ in range(4):
                    for _ in range(nloop):
                            _tmp.append(randint(start,stop))

                    x.append(_tmp)
                    _tmp = []

    else:
            for _ in range(4):
                    for _ in range(nloop):
                            _tmp.append(round(uniform(start,stop),1))

                    x.append(_tmp)
                    _tmp = []


    x1,x2,x3,x4 = x
    lines1 = list(zip(x1,x2))
    lines2 = list(zip(x3,x4))

    for coord in range(nloop):

            line1,line2 = lines1[coord],lines2[coord]

            if isOverlap(line1,line2):
                    print(f'V [YES] The Line 1 {str(line1)} overlaps the Line 2 {str(line2)}')
            else:
                    print(f'X [NOT] The Line 1 {str(line1)} not overlaps the Line 2 {str(line2)}')