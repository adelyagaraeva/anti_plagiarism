
with open('input.txt', 'r', encoding='utf-8') as f:
    l = []
    for i in f:
        l.append(i.split())
    max9 = 0
    max10 = 0
    max11 = 0
    i9 = 0
    i10 = 0
    i11 = 0
    for i in l:
        if (i[2] == '9'):
            max9 += int(i[3])
            i9 += 1
        elif (i[2] == '10'):
            max10 += int(i[3])
            i10 += 1
        elif (i[2] == '11'):
            max11 += int(i[3])
            i11 += 1
    print(max9/i9, max10/i10, max11/i11)
