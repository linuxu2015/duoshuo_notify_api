#!/usr/bin/env python
#coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
import get_duoshuo
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
        get_duoshuo.get_newdata()
        return jsonify({'resp':status})
    elif request.method == 'GET':
        return jsonify({'resp':errstatus})
    else:
        return jdonigy({'resp':'unknown method'})


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0',debug=True)
