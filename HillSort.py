import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(5, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def Hill_Sort(alist):
	length = len(alist)
	gap  = length // 2 
	while gap > 0:
		for i in range(gap,length):
			while i >= gap and alist[i] < alist[i-gap]:
				alist[i],alist[i-gap] = alist[i-gap],alist[i]
				i -= gap
		gap = gap // 2

if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = sorted(l)
		Hill_Sort(l)
		print(l == standard_l)

