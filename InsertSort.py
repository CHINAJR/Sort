import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(0, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def InertSort(alist):
	length = len(alist)
	for i in range(1,length):
		for j in range(i,0,-1):
			if alist[j] < alist[j-1]:
				alist[j],alist[j-1] = alist[j-1],alist[j]

if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = sorted(l)
		InertSort(l)
		print(l == standard_l)

