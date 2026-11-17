from flask import Flask, redirect, render_template, request
from models.article import Article
from services.reference_service import reference_service

app = Flask(__name__)


@app.route("/")
def index():
    example = Article(
        "Mbiazi, Dave and Bhange",
        "Survey on AI Ethics: A Socio-Technical Perspective",
        "Computational Intelligence",
        "2025",
        "41",
        "6",
        "e70149",
    )
    example2 = Article("HYY", "ollaan köyhiä", "ylioppilaslehti", "2025")
    articles = [example, example2]

    return render_template("index.html", references=articles)


@app.route("/add_article", methods=["POST"])
def add_reference():
    author = request.form.get("author")
    title = request.form.get("title")
    journal = request.form.get("journal")
    year = request.form.get("year")

    volume = request.form.get("volume")
    number = request.form.get("number")
    pages = request.form.get("page_a", ""), request.form.get("page_b", "")

    month = request.form.get("month")
    note = request.form.get("note")

    doi = request.form.get("doi")
    issn = request.form.get("issn")
    zblnumber = request.form.get("zblnumber")
    eprint = request.form.get("eprint")

    reference_service.create_reference(author, title, journal, year, volume, number, pages, month, note)

    return redirect("/")
