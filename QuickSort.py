import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(5, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def QuickSort(alist,start,end):
	if start >= end :
		return
	low = start
	high = end 
	mid = alist[low]

	while high > low:
		while high > low and alist[high] >= mid:
			high -= 1
		alist[low] = alist[high]
		while high > low and alist[low] <= mid:
			low += 1
		alist[high] = alist[low]
	alist[low] = mid
	QuickSort(alist,start,low-1)
	QuickSort(alist,high+1,end)

if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = sorted(l)
		QuickSort(l,0,len(l)-1)
		print(l == standard_l)

