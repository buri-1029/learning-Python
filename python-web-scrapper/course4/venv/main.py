from flask import Flask, render_template, request

app = Flask("SuperScrapper")

# @는 바로 아래에 있는 함수만을 찾으며, 함수를 deco 해주는 역할
@app.route("/")
def main():
    return render_template("main.html")


@app.route("/search")
def search():
    word = request.args.get('word')
    #return f"You are looking for a job in {word}"
    return render_template("result.html",searchingBy=word, test="hi")


# @app.route("/<username>")
# def hello(username):
#     return f"Hello {username} !"


# 웹 서버 생성
app.run(host="127.0.0.1")
