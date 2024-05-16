n = 3
m = 2

dp = [ [0]*n for i in range(m)]

for i in range(n):
    dp[0][i] = 1

print(dp)
