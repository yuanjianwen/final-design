
# coding: utf-8

# In[1]:


import sys
import requests
#import urllib
import time


# In[2]:


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
}
url = 'https://detail.tmall.com/item.htm?spm=a1z10.4-b.w13891609-17540690231.2.43891a00lHOCHj&id=541901696831&scene=taobao_shop'


# In[3]:


data = requests.get(url, headers=headers)


# In[4]:


data.status_code


# In[5]:


data.encoding


# In[6]:


#soup = BeautifulSoup(data.text, "html.parser", from_encoding='utf-8')
from lxml import etree
selector = etree.HTML(data.text)


# In[7]:


comments = selector.xpath('//tr')


# In[8]:


users = []
col_meta = []
comment_texts = []

#遍历
for comment in comments:
    user = comment.xpath('//tr/[@ class="col-meta"/text]')
    col_meta = comment.xpath('.//tr/dr[@class = "tm-rate-fulltxt"]/text')
    comment_text = comment.xpath('.//p/text()')[0].strip()
    
    users.append(user)
    col_meta.append(star)
    comment_texts.append(comment_text)

comment_dic = {'user':users, 'col_meta':col_meta, 'comments':comment_texts}


# In[9]:


import pandas as pd
comments_df = pd.DataFrame(comment_dic)


# In[10]:


comments_df


# In[11]:


import requests
import re

# 创建循环链接
urls = []
for i in list(range(1,1000)):
    urls.append('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.11.38ba4ac4YT1FcG&id=567355050426&skuId=3613268733846&user_id=196993935&cat_id=53596001&is_b=1&rn=38894e947eed21043201afaf661e0393' %i)

# 构建字段容器
nickname = []
ratedate = []
color = []
size = []
ratecontent = []

# 循环抓取数据
for url in urls:
    content = requests.get(url).text

# 借助正则表达式使用findall进行匹配查询
    nickname.extend(re.findall('"displayUserNick":"(.*?)"',content))
    color.extend(re.findall(re.compile('颜色分类:(.*?);'),content))
    size.extend(re.findall(re.compile('尺码:(.*?);'),content))
    ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'),content))
    ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'),content))
    print(nickname,color)

# 写入数据
file = open('南极人天猫评价.csv','w')
for i in list(range(0,len(nickname))):
    file.write(','.join((nickname[i],ratedate[i],color[i],size[i],ratecontent[i]))+'\n')
file.close()


# In[ ]:


#!/usr/bin/python


import requests;

import json;


for m in range(1,100):

    url ="https://rate.tmall.com/list_detail_rate.htm?itemId=531867931310&spuId=574477483&sellerId=2888462616&order=3&currentPage="+str(m)


    res=requests.get(url).text[12:-1]

    # print(res)

    # print(type(res))

    a=json.loads(res)

    b=a["rateDetail"]["rateList"]

    for i in b:
        try:


            with open("a.txt","a+") as f:

               f.write( i["rateContent"])+"\n"

        except:

            continue;


# In[ ]:


import requests

