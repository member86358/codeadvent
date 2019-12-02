import math

filename = "puzzle input.txt"
file_object  = open(filename, 'r') 

f = 0
for line in file_object:
	res = (int(line) / 3)
	floorednum = math.floor(res)	
	finalres = floorednum - 2

	f += finalres
	print(finalres)
	print(f)






