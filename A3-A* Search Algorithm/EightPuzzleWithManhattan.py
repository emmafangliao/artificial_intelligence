from EightPuzzle import *

correct = [[0,1,2],[3,4,5],[6,7,8]]

def h(s):

	distance=0

	for i in range(3):
		for j in range(3):
			if s.b[i][j] != correct[i][j] and s.b[i][j] != 0:
				tile = s.b[i][j]
				remainder = tile % 3
				div = (tile-remainder) / 3
				dist = abs(i-div) + abs(j-remainder)
				distance += dist

	return distance
