l= [int(x) for x in (input("enter list for finding max product of subarrays:")).split()]
l1=[]
for i in range(len(l)):
    for j in range(i+1, len(l)+1):
        l1.append(l[i:j])
    if l1[i] == l:
        l1.remove(l1[i])
print(l1)
x=1
l2=[]
for i in l1:
    for j in range(len(i)):
        x *= i[j]
    l2 += [x]
    x = 1
print(f"maximum value of products of elements of subarrays:{max(l2)}")
