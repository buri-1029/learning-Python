from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {} # fake db : 서버 메모리에 있는,

# @는 바로 아래에 있는 함수만을 찾으며, 함수를 deco 해주는 역할
@app.route("/")
def main():
    return render_template("main.html")


@app.route("/search")
def search():
    # word를 query arguments에서 찾는데,
    word = request.args.get('word')
    if word:
        word = word.lower()  # 소문자로 변환
        # print(jobs)

        # 누군가 'python'을 검색했었다면,
        # 또 다른 누군가 같은 단어를 검색해도 fake DB에 
        # 해당 단어가 저장되어 있기 때문에 스크래퍼를 안 돌려도 된다. 
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")

    # rendering 작업
    return render_template("result.html", searchingBy=word,
      resultNumber=len(jobs), jobs=jobs, test="hi")
    # return f"You are looking for a job in {word}"

@app.route("/export")
def export():
    # try 블록 안 어디서든 Exception raise되면
    # 그 결과로, except 문 안의 redirect("/")가 실행
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


# @app.route("/<username>")
# def hello(username):
#     return f"Hello {username} !"


# 웹 서버 생성
app.run(host="127.0.0.1")
