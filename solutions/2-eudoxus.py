
t = int(input())

cases = []
for j in range(t):
	cases.append(int(input()))

#cases = [2,4,5]


def eudoxus(n):
	a,b = 1,0
	for _ in range(n):
		c = a+b
		d = c+b
		a,b = d,c
	return a,b


for i in cases:
	print(eudoxus(i))
