from flask import Flask, redirect, render_template, request
from models import Article
app = Flask(__name__)

@app.route("/")
def index():
    example = Article("Mbiazi, Dave and Bhange", "Survey on AI Ethics: A Socio-Technical Perspective", "Computational Intelligence", "2025", "41", "6", "e70149")
    example2 = Article("HYY", "ollaan köyhiä", "ylioppilaslehti", "2025")
    articles = [example, example2]

    return render_template("index.html", references=articles)

@app.route("/add_article", methods=["POST"])
def add_reference():
    author = request.form.get("author") or None
    title = request.form.get("title") or None
    journal = request.form.get("journal") or None
    year = request.form.get("year") or None

    volume = request.form.get("volume") or None
    number = request.form.get("number") or None
    pages = (
        request.form.get("page_a") or "",
        request.form.get("page_b") or ""
    )

    month = request.form.get("month") or None
    note = request.form.get("note") or None

    doi = request.form.get("doi") or None
    issn = request.form.get("issn") or None
    zblnumber = request.form.get("zblnumber") or None
    eprint = request.form.get("eprint") or None



    return redirect("/")
