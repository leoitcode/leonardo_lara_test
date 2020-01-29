from overlap import isOverlap
from subprocess import Popen

import re
import sys
import ast

#Main Process
if __name__ == '__main__':

	#Get the current file name
	filename = sys.argv[0]


	try:

		#Get the input coordinates
		coord1 = input("Enter the x-axis coordinates of the Line 1 [Format: (x1,x2)]: ")
		coord2 = input("Enter the x-axis coordinates of the Line 2 [Format: (x3,x4)]: ")

		#Create a regex pattern: (number,number)
		pattern = re.compile("(\(\d+\.?\d*,\d+\.?\d*\))")

		
		#Check if the first line coordinates are in the pattern
		if not pattern.match(coord1):

			#If it isn't in the pattern restart python program
			print("These coordinates aren't on pattern (x1,x2)")
			p = Popen("python3 " + filename, shell=True)
			p.wait()


		#Check if the second line coordinates are in the pattern
		if not pattern.match(coord2):

			#If it isn't in the pattern restart python program
			print("These coordinates aren't on pattern (x3,x4)")
			p = Popen("python3 " + filename, shell=True)
			p.wait()
			
		#Transform the string meaning to tuple type
		coord1,coord2 = ast.literal_eval(coord1),ast.literal_eval(coord2)

		#Check if the lines are overlaped
		if isOverlap(coord1,coord2):
			print("These lines are overlaped!")
			
		else:
			print("These lines are not overlaped!")


	except Exception as e:

		print('There is something wrong with coordinates try again.')
		print(f'Error: {e}')
		p = Popen("python3 " + filename, shell=True)
		p.wait()










