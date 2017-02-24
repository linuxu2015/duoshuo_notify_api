#!/usr/bin/env python
# coding:utf-8
import  requests
import json
def get_newdata():
    uro = 'your duoshuo api'
    res = requests.get(url)
    data = json.loads(res.text)
    num = len(data['response'])
    newest_data = data['response'][num-1]['meta']
    art_url = newest_data['thread_key']
    author_name = newest_data['author_name']
    time = newest_data['message']
    ##下面就可以按你自己的方式处理获取到的最新的评论内容了

