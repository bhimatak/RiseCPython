str1 = "abcdef"
str2 = "bcdfgh"

s1 = set(str1)
s2 = set(str2)

common = s1 & s2
# print(common)

# ret = ""
# for ch in str1:
#     if ch not in common:
#         ret += ch
# print(ret)
# for ch in str2:
#     if ch not in common:
#         ret += ch

ret = [ch for ch in str1 if ch not in common]+[ch for ch in str2 if ch not in common]
print(''.join(ret))
# result = [ch for ch in str1]
# print(result)
