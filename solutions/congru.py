

x0 = 4
print(x0)
a = 5
c = 7
m = 8
ri = []

i = 8
xn = (a*x0+c) % m
ri.append(xn/m)
while i > 0:
    print(xn)
    xn = (a*xn+c) % m
    ri.append(xn/m)
    i -= 1

print(ri)
