n = 4
res = 0

for i in range(32):
    bit = (n >> i) & 1
    res = res | (bit << (31 - i))    

print(res)
print(2**29)