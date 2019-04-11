import re


pattern = r'ab(?P<dog>c)d(?P<pig>ef)'
regex = re.compile(pattern)

match_obj = regex.search('abcdefghijklmnopqrstuvwxyz')
print(list(filter(lambda x: '__' not in  x, dir(match_obj))))
# attributes
print(match_obj.pos)  # 匹配目标的开始位置
print(match_obj.endpos)  # 匹配目标的结束位置
print(match_obj.re)  # 正则表达式
print(match_obj.string)  # 目标字符串
print(match_obj.lastgroup)  # 最后一组组名
print(match_obj.lastindex)  # 最后一组是第几组
print(match_obj.regs)  #

# methods
print(match_obj.start())
print(match_obj.end())
print(match_obj.group())  # 获取整个内容
print(match_obj.group(1))  # 获取子组1匹配到的内容
print(match_obj.group(2))  # 获取子组1匹配到的内容
print(match_obj.group('pig'))  # 获取组‘pig’匹配到的内容
print(match_obj.groups())  # 获取所有子组匹配到的内容
print(match_obj.groupdict())  # 获取所有捕获组子组匹配到的内容字典, 只能获取捕获组
