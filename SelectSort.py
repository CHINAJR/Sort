import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(0, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def SelectSort(alist):
	length = len(alist)
	for i in range(length-1):
		mins = i
		for j in range(i+1,length):
			if alist[j] < alist[mins]:
				mins = j
		#if mins != i:
		alist[i],alist[mins] = alist[mins],alist[i]
if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = sorted(l)
		SelectSort(l)
		print(l == standard_l)
	#li = [54,26,93,17,77,31,44,55,20]
	
