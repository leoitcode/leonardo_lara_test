import ast
import sys

from overlap import overlap_test
from subprocess import Popen

#Main Process
if __name__ == '__main__':

        
    # Get the current file name
    filename = sys.argv[0]
    exit = False

    def check_input(*args):

        ''' Check if each arg (start,stop,nloop) is a interger or float and convert
            INPUT: Arguments to be analyzed
            OUTPUT: List with converted strings
        '''
        
        global exit

        _tmp = []

        sys.exit() if exit else None

        for entry in args:

            try:
                entry = int(entry)
                _tmp.append(entry)

            #If it's not a int
            except ValueError:

                try:
                    entry = float(entry)
                    _tmp.append(entry)

                #If it's not a float
                except ValueError:

                    print("No.. input is not a number. Try again")

                    # Subprocess reopening the test.py
                    p = Popen("python3 " + filename, shell=True)
                    p.wait()
                    exit = True

        return _tmp


    start = input("Enter the start point for testing: ")
    stop = input("Enter the end point for testing: ")
    nloop = input("Enter the quantity of tests: ")

    start,stop,nloop = check_input(start,stop,nloop)

    sys.exit() if exit else None

    overlap_test(start,stop,nloop)