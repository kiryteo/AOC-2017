
def main():

	#x = int(x)
	q = [int(x) for x in input()]
	
	z = int(len(q))
	f = int(z / 2)
	i = 0
	i = int(i)
	sum = 0
	for i in range(f) :
		if q[i] == q[i+f]:
			sum = sum + (q[i] * 2)
	print (sum)

main()