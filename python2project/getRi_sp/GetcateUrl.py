# -*- coding:UTF-8 -*-
# 爬取网址：www.listenerri.com
# 爬取android分类的第一页内容，并分别存储为对应文件
# 2017-10-07
import re
import urllib2
import urllib

url = "http://www.listenerri.com/categories/android/"
url_earlypart = "http://www.listenerri.com"
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
request = urllib2.Request(url,headers=ua_headers)
response = urllib2.urlopen(request)
html = response.read()
p_time_content = re.compile('<a\sclass=\"post-title-link\"\shref=\"(.*?)\"',re.S)
mtc = p_time_content.findall(html)
# url_latterpart = []

url_full = []
for item in mtc:
    item = urllib.quote(item)
    url_full.append(url_earlypart+item)
    # url_latterpart.append(item)
# print url_full[0]
p_content = re.compile(r'<span\sitemprop="name">(.*?)</span>', re.S)
mc = p_content.findall(html)
filenames = []
for item in mc:
    filenames.append(item)
i=0
for urliter in url_full:
    # print type(urliter)
    # print urliter
    requestl = urllib2.Request(urliter,headers=ua_headers)
    htmliter = urllib2.urlopen(requestl).read()
    # print htmliter
    filename = filenames[i]
    with open(filename,"w+") as f:
        f.write(htmliter)
        print filename+"-"*16+"Save Success！"
    i += 1
# print url_full.__len__()
# p_time = re.compile('<a\sclass=\"post-title-link\"\shref=\"(.*?)\"',re.S)
# mt = p_time.findall(html)
# for item in mt:
#     print item
# p_content = re.compile(r'<span\sitemprop="name">(.*?)</span>',re.S)
# mc = p_content.findall(html)
# for item in mc:
#     print item