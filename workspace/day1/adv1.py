import math

def main():
	
	z = [int(x) for x in input()]
	q = []
	for i in range(len(z)-1):
		if z[i] == z[i+1]:
			q.append(z[i])
			
	if z[len(z)-1]==z[0]:
		q.append(z[0])
	
	#print (q[len(z)-1])
	k = sum(q)
	print (k)				
				
main()