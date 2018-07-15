import random
def GenerateRandomArray(size,maxnum):
	n = []
	size = random.randint(1,size)
	for i in range(size):
		n.append(random.randint(1,maxnum))
	print(n)

if __name__ == '__main__':
	for i in range(10):
		GenerateRandomArray(5,10)
