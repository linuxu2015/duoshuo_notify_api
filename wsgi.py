#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask
from flask import jsonify
from flask import request
import get_duoshuo
import tomail
app = Flask(__name__)
status = [
    {
        'status': 200,
        'info': '发送成功'
    }
]
errstatus = [
    {   
        'status': 201,
        'info': '不支持GET方式'
    }
]

@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        tos = request.form.get('action')
        sig = request.form.get('signature')
      #  print tos,sig
        newest = get_duoshuo.get_newdata()
     #   print newest
        #print newest[2]
        data = newest[1]+ 'http://www.linuxu.top/' + newest[0] +'  :'+ newest[2]
    #    print data
        #print data
        tomail.email(data)

        return jsonify({'resp':status})
    elif request.method == 'GET':
        return jsonify({'resp':errstatus})
    else:
        return jdonigy({'resp':'unknown method'})


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0',debug=True)
