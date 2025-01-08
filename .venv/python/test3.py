#given string is palindrome or not
'''s=input('Enter String:')
r=s[::-1]
if s==r:
    print('s is pallindrome')
else:
    print('s is not a pallindrome')'''

#highest value in list
'''l=[1,2,3,4,8,5,6,7,9]
m=max(l)
print(m)
l=[1,2,3,8,4,5,6,7,9]
hig=0
for i in range(len(l)):
    if l[i]>hig:
        hig=l[i]
print(hig)'''

#second highest value in list
'''l=[1,2,3,8,4,5,6,7,9]
''hig=0
for i in range(len(l)):
    if l[i]>hig:
        hig=l[i]
l.remove(hig)
hig=0
for i in range(len(l)):
    if l[i]>hig:
        hig=l[i]
print(hig)''
#l.sort()
#print(l[-2])
l1=sorted(l)
#print(l1[-2])
print(l.index(l1[-2]))'''

#least value in list
'''l=[1,2,3,0,8,4,5,6,7,9]
l1=sorted(l)
print(l1[0])'''

#Input:- aaabbcccdaabbb Output:-3a2b3c1d2a3b
'''s=input('Enter String:')
s1=''
n=1
for i in range(len(s)):
    if i<len(s)-1 and s[i]==s[i+1]:
        n+=1
    else:
        s1+=str(n)+s[i]
        n=1
print(s1)'''

#Input:- ['kumar', 'somu', 'sonu', 'ram', 'raju'], Output:- {'k': 1, 's': 2, 'r': 2}
'''l=['kumar', 'somu', 'sonu', 'ramu', 'raju']
d={}
for i in l:
    if i[0] not in d:
        d[i[0]]=1
    else:
        d[i[0]]+=1
print(d)'''

#sort array without using built-in methods(bubble sort)
'''l=[12,45,87,43,16]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)'''

#sort numbers in list without using built-in methods(selection sort)
'''l=[8,6,5,4,3]
for i in range(len(l)-1):
    s=i
    for j in range(i+1,len(l)):
        if l[s]>l[j]:
            s=j
    l[i],l[s]=l[s],l[i]
print(l)'''

#nested list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(nested_list[1][2])