import math
import time
filename = "puzzle input.txt"
n = []
file_obj = open(filename, 'r')

def foo(a):
    for b in a:
        yield b

def calcfuel(mass):
	return math.floor((mass) / 3) - 2
	
def isDone(result):
	if result != None and result != -1:
		return False
	else:
		return True

lst = []
lstTotal = []
f = 0
ret_val = 0
temp = 0
for lines in file_obj:
	temp += 1
	if lines.strip():
		integer = int(lines)
	ret_val = calcfuel(integer)
	lst.append(ret_val)
	if not isDone(ret_val):
		ret_val = (calcfuel(ret_val))
		lst.append(ret_val)
		if not isDone(ret_val):
			ret_val = (calcfuel(ret_val))
			lst.append(ret_val)
			if not isDone(ret_val):
				ret_val = (calcfuel(ret_val))
				lst.append(ret_val)
				if not isDone(ret_val):
					ret_val = (calcfuel(ret_val))
					lst.append(ret_val)
					if not isDone(ret_val):
						ret_val = (calcfuel(ret_val))
						lst.append(ret_val)
						if not isDone(ret_val):
							ret_val = (calcfuel(ret_val))
							lst.append(ret_val)
							if not isDone(ret_val):
								ret_val = (calcfuel(ret_val))
								lst.append(ret_val)
								if not isDone(ret_val):
									ret_val = (calcfuel(ret_val))
									lst.append(ret_val)
									if not isDone(ret_val):
										ret_val = (calcfuel(ret_val))
										lst.append(ret_val)


	del lst[-1]
#	print(lst)
	print(temp)
#	time.sleep(1)
	lstTotal.append(sum(lst))
	del lst[:]
	print(lstTotal)

print(sum(lstTotal))












