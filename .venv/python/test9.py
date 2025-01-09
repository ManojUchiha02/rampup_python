"""01) Given an array nums of distinct integers, return all the possible Permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]"""
l = [int(x) for x in (input("enter list:")).split()]
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
