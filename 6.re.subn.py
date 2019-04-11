import re


s = 'hello world  nihao  china'
t = re.subn(r'\s+', repl='#', string=s)
print(t)

