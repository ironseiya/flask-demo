# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/hello") #不兼容最后斜杠
def hello():
    return "hello world"


app.run(debug=True)
