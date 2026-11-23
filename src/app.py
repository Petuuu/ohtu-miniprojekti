"""Defines the Flask routes for the application."""

import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, flash

from services.reference_service import reference_service

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    references = reference_service.get_references()
    return render_template("index.html", references=references)


@app.route("/add_reference", methods=["POST"])
def add_reference():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    journal = request.form.get("journal")
    year = request.form.get("year")

    volume = request.form.get("volume")
    number = request.form.get("number")
    pages = request.form.get("pages")

    month = request.form.get("month")
    note = request.form.get("note")

    doi = request.form.get("doi")
    issn = request.form.get("issn")
    zblnumber = request.form.get("zblnumber")
    eprint = request.form.get("eprint")
    try:
        reference_service.create_reference(
            key,
            author,
            title,
            journal,
            year,
            volume,
            number,
            pages,
            month,
            note,
            doi,
            issn,
            zblnumber,
            eprint,
        )
    except ValueError:
        flash("Input was too long")

    return redirect("/")

@app.route("/<key>/delete", methods=["POST"])
def remove_reference(key):
    try:
        reference_service.remove_reference(key)
    except KeyError:
        flash(f"No reference with key '{key}'")
    return redirect("/")
