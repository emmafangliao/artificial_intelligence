from EightPuzzle import *

correct = [[0,1,2],[3,4,5],[6,7,8]]

def h(s):
	'''return the number of tiles that are out of place i.e. different from the goal state as defined
	in correct above (a list of lists). this is the hamming distance.'''
	tiles=0

	for i in range(3):
		for j in range(3):
			if s.b[i][j] != correct[i][j] and s.b[i][j] != 0:
				tiles += 1

	return tiles 



