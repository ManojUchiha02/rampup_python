"""
09) Given two strings s and t of lengths m and n respectively, return the minimum window 
Substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique.
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string
"""
def minWindow(s, t):
    if not s or not t:
        print("enter valid strings")
    d={}; x=0
    for i in t:
        d[i]=t.count(i)
    a,b = 0,0; i=float("inf")
    l=0; y=(0,0); d1={}
    while b<len(s):
        c=s[b]
        d1[c]=d1.get(c, 0) + 1
        if c in d and d1[c]==d[c]:
            l+=1
        while a<=b and l==len(d):
            c=s[a]
            if b-a+1<i:
                x=b-a+1
                y=(a,b)
            d1[c] -= 1
            if c in d and d1[c]<d[c]:
                l -= 1
            a += 1
        b += 1
    u,v = y
    return s[u:v+1] if x != float("inf") else ""
s = input("add string for checking minwindow:")
t = input("enter substring with elements of minwindow:")
print(minWindow(s, t))
