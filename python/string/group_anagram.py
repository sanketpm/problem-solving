'''
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

from collections import defaultdict

res = {}
strs = ["eat","tea","tan","ate","nat","bat"]

for s in strs:
    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1
    
    if not tuple(count) in res:
        res[tuple(count)] = []
    
    res[tuple(count)].append(s)

print(res.values())