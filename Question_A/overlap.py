import numpy as np

from random import *
from datetime import datetime as dtt


# Seed random number generator
seed(dtt.now())

def isOverlap(line1,line2):

    ''' This function check if two lines are overlapped
        Input: 2 tuples containing the coordinates
        Output: True -> Are overlapped
        False -> Not overlaped
    '''
    
    # Get all coordinates
    line1,line2 = sorted(line1),sorted(line2)

    x1,x2,x3,x4 = line1+line2

    overlap = min(x2, x4) - max(x1, x3)

    # Returns True if was found some intersection between lines, or False
    return True if overlap >=0 else False



def overlap_test(start,stop,nloop):

    ''' This function test a variety of lines pairs.
        Input: Range of work (Start, Stop) and How many tests
        Output: Print the result
    '''

    # List X for append many _tmp lists
    x,_tmp = [],[]

    # Create four lists with a Random int or float numbers
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

    # Unpack the four lists into x variables
    x1,x2,x3,x4 = x

    # Zip lists to create lines
    lines1 = list(zip(x1,x2))
    lines2 = list(zip(x3,x4))

    for coord in range(nloop):

        line1,line2 = lines1[coord],lines2[coord]

        # Check if lines are overlapped
        if isOverlap(line1,line2):
            print(f'V [YES] The Line 1 {str(line1)} overlaps the Line 2 {str(line2)}')
        else:
            print(f'X [NOT] The Line 1 {str(line1)} not overlaps the Line 2 {str(line2)}')