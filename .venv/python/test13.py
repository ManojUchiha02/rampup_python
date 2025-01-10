"""Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]"""
l= input("enter string to check for palindrome sublists:")
l1=[]
l2=[]
for i in range(len(l)):
    for j in range(i+1, len(l)+1):
        l1.append(l[i:j])
    if len(l) != 1 and l1[i] == l:
        l1.remove(l1[i])
print(l1)
for i in l1:
    if i == i[::-1]:
        l2 += [i]
print(f"all possible pallindrome sublists:{l2}")
