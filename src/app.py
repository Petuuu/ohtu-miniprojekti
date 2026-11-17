from flask import Flask, redirect, render_template
from models import article
app = Flask(__name__)

@app.route("/")
def index():
    example = article.Article("Mbiazi, Dave and Bhange", "Survey on AI Ethics: A Socio-Technical Perspective", "Computational Intelligence", "2025", "41", "6", "e70149")
    example2 = article.Article("HYY", "ollaan köyhiä", "ylioppilaslehti", "2025")
    articles = [example, example2]

    return render_template("index.html", references=articles)

