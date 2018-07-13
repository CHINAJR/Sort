def Bubble_Sort(alist):
	length = len(alist)
	for i in range(length-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				alist[j],alist[j+1] = alist[j+1],alist[j]
        
        
        
        
if __name__ == '__main__':
	li = [54,26,93,17,77,31,44,55,20]
	Bubble_Sort(li)
	print(li)
