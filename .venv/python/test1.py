#Factorial
'''n=int(input('n:'))
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)'''

#remove duplicates in list
'''l=[1,1,2,3,5,3]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)'''

#remove duplicates in string
'''s='asdfzxcfdsa'
s1=''
for i in s:
    if i not in s1:
        s1+=i
print(s1)'''

#print most repeated character in string
'''s='asadfzxcafdsa'
d={}
for i in s:
    ''if i not in d:
        d[i]=s.count(i)''
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
m=max(d.values())
for a,b in d.items():
    if m==b:
        print(f'{a}:{b}')'''

#print most repeated word in sentence
'''sen='BOSS OF BOSS OF BOSSES'
w=sen.split()
print(f'w:{w}')
d={}
for i in w:
    ''if i not in d:
        d[i]=1
    else:
        d[i]+=1''
    if i not in d:
        d[i]=w.count(i)
print(f'd:{d}')
m=max(d.values())
for a,b in d.items():
    if b==m:
        print(a)'''

#addition without apppend
'''l=[1,2,3]
#l=l+[4]
#l[:0]=[4,5]
#l[3:]=[4,5,6]
#l[len(l):]=[4,5,6,7,8]
l[1]=5
print(l)'''

#most repeated characetr
s='aaabbbbcccccc'
d={}
for i in s:
    if i not in d:
        d[i]=s.count(i)
m=max(d.values())
for a,b in d.items():
    if b==m:
        print(f'{a}:{b}')