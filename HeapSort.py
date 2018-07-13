import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(5, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def Heap_sort(alist):
	size = len(alist)
	for i in range(0,(int(size/2)))[::-1]:
		adjust_heap(alist,i,size)
	for i in range(0,size)[::-1]:
		alist[i],alist[0] = alist[0],alist[i]
		adjust_heap(alist,0,i)
	return alist

def adjust_heap(alist,i,size):
	lchild = i*2+1
	rchild = i*2+2
	maxs = i
	if  i < size/2:
		if lchild < size and alist[lchild] > alist[maxs]:
			maxs = lchild
		if rchild < size and alist[rchild] > alist[maxs]:
			maxs = rchild
		if maxs != i:
			alist[i],alist[maxs] = alist[maxs],alist[i]
			adjust_heap(alist,maxs,size)



if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = sorted(l)
		a = Heap_sort(l)
		print(a == standard_l)


