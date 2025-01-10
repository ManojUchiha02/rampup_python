"""10) Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]"""
l = [int(x) for x in (input("enter list of 0,1,2 elements:")).split()]
a = l.count(0)
b = l.count(1)
c = l.count(2)

x = 0
l1 = []
for i in a,b,c:
    for j in range(0,i):
        l1 += [x]
    x += 1
print(l1)