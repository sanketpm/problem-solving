
print("a" in "abcdefghijklmnopqrstuvwxyz")

print(ord("a") >= 95 and ord("a") <= 122)
print(ord("0") >= 48 and ord("0") <= 57)
print("A".lower())


s = "A man, a plan, a canal: Panama"
s = "0P"
s = "ab_a"

l = 0
r = len(s) - 1

print('_', ord("_"))
print('a', ord('a'))

# while l <= r:
#     lchar = (s[l].lower())
#     rchar = (s[r].lower())
    
#     print(s[l], ord(s[l].lower()))
#     print(s[r], ord(s[r].lower()))

#     l_ascii = ord(s[l].lower())
#     r_ascii = ord(s[r].lower())

#     while l < r and not (l_ascii in range(95, 123) or l_ascii in range(48, 58)):
#         l += 1
#         l_ascii = ord(s[l].lower())
        
    
#     while l < r and not (r_ascii in range(95, 123) or r_ascii in range(48, 58)):
#         r -= 1
#         r_ascii = ord(s[r].lower())

#     if l_ascii != r_ascii:
#         print("False")
#         break
#     else:
#         l += 1
#         r -= 1

# print(True)