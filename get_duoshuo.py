#!/usr/bin/env python
# coding:utf-8
import  requests
import json
import config
def get_newdata():
    url = config.duoshuo_api_url
    print url
    res = requests.get(url)
    data = json.loads(res.text)
    num = len(data['response'])
    newest_data = data['response'][num-1]['meta']
    art_url = newest_data['thread_key']
    author_name = newest_data['author_name']
    message = newest_data['message']
    data = [art_url,author_name,message]
    return data 
    ##下面就可以按你自己的方式处理获取到的最新的评论内容了

