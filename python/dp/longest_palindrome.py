s = 'abccbd'
n = len(s)

print(s)
print(n)

dp = [[False] * n for _ in range(n)]

res = [0, 0]

for i in range(n):
    dp[i][i] = True

for i in range(n - 1):
    s_i = s[i: i + 2]
    
    if s[i] == s[i + 1]:
        dp[i][i + 1] = True
        res = [i, i + 1]
    
for diff in range(2, n):
    for i in range(n - diff):
        j = i + diff

        s_i_j = s[i:j + 1]

        if s[i] == s[j] and dp[i + 1][j - 1]:
            dp[i][j] = True
            res = [i, j]

i, j = res[0], res[j]

res_str = s[i: j + 1]