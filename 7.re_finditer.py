import re


it = re.finditer(r'\d+', '2008-2018 10年， 中国发生量翻天覆地的变化')
for i in it:
    print(i.group())

