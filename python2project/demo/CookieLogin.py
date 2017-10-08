# -*- coding: UTF-8 -*-
import urllib2
url = "http://www.renren.com/959765392/profile"

headers={
    "Host" : "www.renren.com",
    "Connection" : "keep-alive",
    # "Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    # "Accept-Encoding" : "gzip, deflate, sdch",
    "Accept-Language" : "zh-CN,zh;q=0.8",
    "Cookie" : "anonymid=j7r4b56q-udd5nb; jebe_key=a9215d61-5846-4948-80ac-aefbd0f262b0%7Ccfcd208495d565ef66e7dff9f98764da%7C1505796422120%7C0; __utma=151146938.263713235.1505796425.1505796425.1505796425.1; __utmz=151146938.1505796425.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; depovince=HEN; _r01_=1; JSESSIONID=abcvT8U1_P1Ui-9dSGR7v; ick_login=41f30112-f1de-4bfa-980f-9633c39f2836; t=83aafe9976238cb6be156272c17287ac2; societyguester=83aafe9976238cb6be156272c17287ac2; id=959765392; xnsid=147ceee5; springskin=set; vip=1; _ga=GA1.2.263713235.1505796425; _gid=GA1.2.1870635491.1507189844; ch_id=10015; ver=7.0; loginfrom=null; Hm_lvt_9d483e9e48ba1faa0dfceaf6333de846=1507189777; Hm_lpvt_9d483e9e48ba1faa0dfceaf6333de846=1507189978; wp_fold=0; jebecookies=c17ca809-5f55-4375-b749-aa9cbb2b988d|||||"
}

request = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(request)

print response.read()