import re


# pattern = r'(ab)cd(ef)'
# s = 'abcdefghijklmn'
#
# # re模块直接调用findall()
# lst = re.findall(pattern, s)
# print(lst)
#
# # 换compile方法调用
# regex = re.compile(pattern)
# l = regex.findall(s)
# l = regex.findall(s, 1, 17)
# print(l)


pattern = r'(ab)cd(ef)'
s = 'abcdefghijklmnabcdef'

# re模块直接调用findall()
lst = re.findall(pattern, s)
print(lst)

# 换compile方法调用
regex = re.compile(pattern)
l = regex.findall(s)
print(l)