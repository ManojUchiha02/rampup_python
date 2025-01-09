c = [int(x) for x in (input("enter coin denominations:")).split()]
money = int(input("enter amount to be divided into denominations:"))
c.sort(reverse=True)
m = money; l = []; d = {}
for i in range(len(c)):
    if c[i] != 0:
        ai = m // c[i]
        bi = m % c[i]
    m = bi
    l += [c[i]*ai]
    d[c[i]] = ai
x = money - sum(l)
if x==0:
    print(d)
else:
    print("-1")
