import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(5, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def Merge(alist):
	n = len(alist)
	if n <= 1:
		return alist
	num = n // 2 
	left = Merge(alist[:num])
	right = Merge(alist[num:])
	result =MergeSort(left,right)
	return result

def MergeSort(left,right):
	result = []
	l,r = 0,0

	while l < len(left) and r <len(right):
		if left[l] <= right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	result += left[l:]
	result += right[r:]
	return result

if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = sorted(l)
		result = Merge(l)
		print( result == standard_l)

