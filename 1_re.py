import re


# 普通字符
res = re.findall('\d+', 'hel23lo123')
res = re.findall('hello', 'hello world')
res = re.findall('你好', '你好北极')

# 或
res = re.findall('he|d', 'hello world')

# .
res = re.findall('f.o', 'foo is not fao')
res = re.findall('你.啊', '你好啊')
res = re.findall('你.', '你好啊')

# ^
res = re.findall('f', 'foo is not fao')
res = re.findall('^f', 'foo is not fao')

# $
res = re.findall('ao$', 'foo is not fao')
res = re.findall('.+.py$', '正则表达式/1_re.py')

# *
res = re.findall('fo*', 'Foooo, fo, f, fooo')

# +
res = re.findall('fo+', 'foooo, fo, foo,, f o')

# ?
res = re.findall('fo?', 'fooo. fo, f,foo')

# {n}
res = re.findall('fo{3}', 'fooo, fo,. fooo, fio')

# {m, n}
res = re.findall('fo{3,4}', 'fooo, fooooo, fofo , foo , fooo')

# [] 匹配字符集
res = re.findall('^[A-Z][ a-z]*', 'I am a boy. I am man')

# [^...] 匹配字符集
res = re.findall('[^ ]+', 'a little boy')

# \d  \D
res = re.findall('\d', '54sada')
# print(res)
res = re.findall('\D', '54sada')

# \w \W
res = re.findall('\w+', 'heldsad+dsa)Fas(*FA*&ASD_ASd?87ad')
res = re.findall('\W', 'heldsad+dsa)Fas(*FA*&ASD_ASd?87ad')

# \s \S
res = re.findall('\w+\s*\w+', 'hello world')
res = re.findall('\w+\S*\w+', 'hello world')

# \b \B
res = re.findall(r'\bis', 'this is a boy')
res = re.findall(r'is', 'this is a boy')
print(res)
