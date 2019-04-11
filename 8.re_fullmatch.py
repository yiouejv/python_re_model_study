import re


obj = re.fullmatch(r'\S+', 'abcdef123#')
print(type(obj))
