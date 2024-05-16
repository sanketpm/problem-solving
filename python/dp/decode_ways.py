def test():
    self.s = '11106'

    res = 0

    def dfs(s):
        n = len(s)

        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if ( s[0] == '1' and s[1] in "0123456979"):
            res += dfs(s[2:])

        elif (s[0] == '2' and s[1] in '0123456' ):
            res += dfs(s[2:])

result = test()

print(result)