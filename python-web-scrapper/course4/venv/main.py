from flask import Flask, render_template, request
from so import get_jobs 

app = Flask("SuperScrapper")

db = {} # fake db

# @는 바로 아래에 있는 함수만을 찾으며, 함수를 deco 해주는 역할
@app.route("/")
def main():
    return render_template("main.html")


@app.route("/search")
def search():
    word = request.args.get('word')
    if word:
        word = word.lower()  # 소문자로 변환
        jobs = get_jobs(word)
        # print(jobs)

        # 4.5 다시 듣기
        fromDB = db.get(word)
        if fromDB:
            jobs = fromDB
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")

    # rendering 작업
    return render_template("result.html", searchingBy=word,
    resultNumber=len(jobs), test="hi")
    # return f"You are looking for a job in {word}"


# @app.route("/<username>")
# def hello(username):
#     return f"Hello {username} !"


# 웹 서버 생성
app.run(host="127.0.0.1")
