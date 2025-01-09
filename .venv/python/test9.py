l = [1]
l1 = []
l2 = []
l3 = []
l4 = []
for i in range(0,len(l)):
    l1 += [l[i]]
    for j in range(0,len(l)):
        if l[j] not in l1:
            l1 += [l[j]]
    l2 += [l1]
    l1 = []
for i in range(len(l2)):
    for j in range(1, len(l2[i])):
        l1 += [l2[i][j]]
    l1 = l1[::-1]
    l3 += [[l2[i][0]]+l1]
    l1 = []
l2 += l3
for i in l2:
    if i not in l4:
        l4 += [i]
print(l4)