import re


obj = re.match(r'foo+', 'foo, Foo on the table')
print(obj.group())
