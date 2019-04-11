import re


# I == IGNORECASE
s = 'hello world'
pattern = r'Hello'
regex = re.compile(pattern, re.I)
s = regex.search(s).group()
print(s)


# S == DOTALL
s = '\n'
pattern = r'.+'
l = re.findall(pattern, s, flags=re.S)
print(l)


# M == MUTILLINE
s = '''hello nihao
hello kitty
你好，中国
'''
pattern = r'^你好.+'
l = re.findall(pattern, s)
print(l)
l = re.findall(pattern, s, flags=re.M)
print(l)

