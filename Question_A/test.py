import ast
import sys

from overlap import overlap_test
from subprocess import Popen

#Main Process
if __name__ == '__main__':

        filename = sys.argv[0]

        def check_input(*args):

                _tmp = []

                for entry in args:

                        try:
                                entry = int(entry)
                                _tmp.append(entry)



                        except ValueError:

                                try:
                                        entry = float(entry)
                                        _tmp.append(entry)

                                except ValueError:

                                        print("No.. input is not a number. Try again")
                                        p = Popen("python3 " + filename, shell=True)
                                        p.wait()

                return _tmp


        start = input("Enter the start point for testing: ")
        stop = input("Enter the end point for testing: ")
        nloop = input("Enter the quantity of tests: ")

        start,stop,nloop = check_input(start,stop,nloop)

        overlap_test(start,stop,nloop)

        raise SystemExit