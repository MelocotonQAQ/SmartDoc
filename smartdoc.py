#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# ztt
import re
import markdown
#读取txt
a=open('srs.txt')
b=a.read()
print(type(b))
abc=markdown.markdown(b)
a.close()

d=open('code.py')
e=d.read()
print(type(e))
efg=markdown.markdown(e)
d.close()
#正则表达式分成一个列表
input=re.findall(u'.*</[^>]+>',abc)
input=re.findall(u'.*</[^>]+>',efg)
#改颜色
for i in range(len(input)):
    if re.search(u'h1',input[i]):
        input[i]='<div  position: absolute style="color:#00FF00">'+input[i]+'</div>'
        print(input[i])
    elif re.search(u'h2',input[i]):
        input[i] = '<div style="color:#0000FF">' + input[i] + '</div>'
    elif re.search(u'<p>',input[i]):
        input[i] = '<div style="color:#FF0000">' + input[i] + '</div>'
#写入HTML文件
GEN_SRS_HTML = "srs.html"
h1 = open(GEN_SRS_HTML, 'w')
for i in range(len(input)):
    h1.write(input[i])

h1.close()

GEN_CODE_HTML = "code.html"
h2 = open(GEN_CODE_HTML, 'w')
for i in range(len(input)):
    h2.write(input[i])

h2.close()

