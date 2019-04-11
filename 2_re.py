import re


res = re.findall(r'\$\d+', '$10')
res = re.findall(r'\bis', 'this is a boy')
res = re.findall(r'\d+', '213124325345jhsdaf1223')
res = re.search(r'(ab)*', 'absababsababasbda').group(0)
res = re.search(r'\S+@\S+\.(cn|com)', 'xxx@qq.com, xxx@qq.cn').group()
res = re.search(r'(?P<dog>ab)cdef', 'abcdefg').group('dog')
print(res)
