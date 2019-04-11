import re


obj = re.search(r'foo', 'Foo foo on the table, foo')
print(obj.group())
