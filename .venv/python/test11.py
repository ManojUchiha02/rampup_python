"""
03) Given an integer array nums, find a subarray that has the largest product, and return the product.The test cases are generated so that the answer will fit in a 32-bit integer.
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
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
