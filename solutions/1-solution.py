#n = int(input())
#h = int(input())

#instr = []
#for j in range(n):
#	instr.append(int(input())

n = 2
h = 8000
instr = [2,-1]

def escalera(instr,h):
	i = 0
	suma = 0
	pasos = 0
	while suma < h:
		suma += instr[i]
		pasos += 1
		i = (i+1) % n
	return pasos

print(escalera(instr,h))
