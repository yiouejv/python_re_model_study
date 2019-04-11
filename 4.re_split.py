import re

s = 'hello  world nihao China'

# 正则表达式切割
l = re.split(r'\s+', s)
print(l)

# 字符串切割
l = s.split(' ')
print(l)

