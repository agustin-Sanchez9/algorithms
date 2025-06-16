nmap = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
    8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
    14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
    20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
}

entry = int(input())
array = []


while entry > 0:
    res = entry % 26
    div = entry // 26
    if res == 0 and div == 1:
        array.append(nmap[26])
        entry = 0
    elif res == 0 and div != 1:
        array.append(nmap[26])
        entry = div - 1
    else:
        array.append(nmap[res])
        entry = div

array = array[::-1]
chain = ''.join(array)
print(chain)
