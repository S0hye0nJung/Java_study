!mkdir .\templates

%%writefile ./templates/Ex01.html
# 형식
# <!DOCTYPE html>
# <html>
# <body>
#     <h2> title : {{ title }}</h2>
#     <h5> data : {{ data }}</h5>
# </body>
# </html>
# 아래 코드 완성하기

import json
from flask import Flask, render_template

app = Flask(__name__)

json_data = '''{
    "main": {
        "title":"main",
        "data":"maindata"
    },
    "stage1": {
        "title":"stage1",
        "data":"stage1data"
    },
    "stage2": {
        "title":"stage2",
        "data":"stage2data"
    }
}'''

json_data = json.loads(json_data)

# https://localhost:5000/
# 출력 예시 
# title : main
# data : maindata

@app.route('/')
def main():
    title = json_data["main"]["title"]
    data = json_data["main"]["data"]
    return render_template('Ex01.html', title=title, data=data)

# https://localhost:5000/stage1
@app.route('/stage1')
def stage1():
    title = json_data["stage1"]["title"]
    data = json_data["stage1"]["data"]
    return render_template('Ex01.html', title=title, data=data)

# https://localhost:5000/stage2
@app.route('/stage2')
def stage2():
    title = json_data["stage2"]["title"]
    data = json_data["stage2"]["data"]
    return render_template('Ex01.html', title=title, data=data)

if __name__ == '__main__':
    app.run()
