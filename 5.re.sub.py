import re


s = 'hello world  nihao  china'
res = re.sub(r'\s+', '#', s)
res = re.sub(r'\s+', '#', s, 2)
print(res)
