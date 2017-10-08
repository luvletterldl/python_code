# -*- coding: UTF-8 -*-
import re

# pattern = re.compile(r"\d+")
#
# s = pattern.match("123456aa78956..0",2,6)
#
# print s.group()
#

# 这个正则有两组([a-z]+) ([a-z]+)，相同的两组，中间用空格分开，后面的参数I表示忽略大小写
pattern = re.compile(r"([a-z]+) ([a-z]+)",re.I)

m = pattern.match("Hello python hello Python")

print m.group()
# 参数为0时，
print m.group(0)
print m.group(1)
print m.group(2)
# print m.group(3)
# 返回下标
print m.span(2)