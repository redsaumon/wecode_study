
from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

# fakeDB는 라우트 외부에 나와있어야 됨. route 안에 있으면 실행될 때마다 초기화됨
# 진짜 db가 아니라 서버 메모리에 있는 fake db라서 재시작 하면 db날아감
db = {}


@app.route("/")  # /라는 주소를 타고 들어오면 아래 함수 실행
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()  #사용자가 PYTHON를 입력할 수도 있으니까
        existingJobs = db.get(word)
        if existingJobs:  #검색한 값은 db에 다 저장. 이미 db에 저장해둔 값이 있다면 새로 검색할 필요 없이 저장값 반환하면 됨
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")  #입력값이 없으면 홈으로 리턴
    return render_template(
        "report.html",
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs = jobs
    )


@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word: # word가 없으면 에러 발생
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/") #에러 들어오면 홈으로 보내줌



app.run(host="0.0.0.0")