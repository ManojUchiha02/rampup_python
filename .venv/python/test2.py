#print most repeated element in list
'''l=[1,1,1,2,3,4,5,6,7,7,8]
d={}
for i in l:
    if i not in d:
        d[i]=l.count(i)
    ''if i not in d:
        d[i]=1
    else:
        d[i]+=1''
print(d)
m=max(d.values())
for a,b in d.items():
    if m==b:
        print(f'{a} is repeated {b} times')'''

#print lengthiest word in sentence
'''sen='BOSS OF BOSS OF BOSSES'
w=sen.split()
print(f'w:{w}')
d={}
for i in w:
    if i not in d:
        d[i]=len(i)
print(f'd:{d}')
m=max(d.values())
for a,b in d.items():
    if b==m:
        print(f'{a}:{b}')'''

#Prime number program
'''n=int(input('n:'))
t=0
for i in range(2,n):
    if n%i==0:
        t=1
if t==0:
    print('n is prime')
else:
    print('n is not prime)'''

#Program to swap two values
'''l=[1,2,3,4,5]
a=int(input('enter 1st position:'))
b=int(input('enter 2nd position:'))
l[a-1],l[b-1]=l[b-1],l[a-1]
print(l)'''

#Factorial
'''n=int(input('enter value of n:'))
fac=1
for i in range(1,n+1):
    fac*=i
print(fac)'''

#Fibonacci
'''a=0
b=1
c=0
n=int(input('1st n values in fib,Enter n:'))
for i in range(1,n+1):
    if i<=2:
        c=i-1
        print(c)
for i in range(0,n-2):
    c=a+b
    a=b
    b=c
    print(c)'''

#Input:- we are the programmers Output:-programmers the are we
'''s=input('')
l1=s.split()
for i in l1[::-1]:
    print(i, end=' ')'''

#Input:- we are the programmers Output:-ew era eht sremmargorp
'''s=input('')
l1=s.split()
for i in l1:
    print(i[::-1], end=' ')'''

#given number is palindrome or not
n=str(input('Enter Value:'))
r=n[::-1]
if n==r:
    print('n is pallindrome')
else:
    print('n is not a pallindrome')