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
    keys = [
        "key",
        "entry_type",
        "address",
        "annote",
        "author",
        "booktitle",
        "chapter",
        "crossref",
        "doi",
        "edition",
        "editor",
        "email",
        "eprint",
        "howpublished",
        "institution",
        "isbn",
        "issn",
        "journal",
        "month",
        "note",
        "number",
        "organization",
        "pages",
        "publisher",
        "school",
        "series",
        "title",
        "type",
        "url",
        "volume",
        "year",
        "zblnumber",
    ]
    args = {}
    for key in keys:
        args[key] = request.form.get(key)

    try:
        reference_service.create_reference(args)
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

@app.route("/<key>/edit", methods=["POST", "GET"])
def edit_reference(key):
    if request.method == "GET":
        reference = reference_service.find_by_key(key)
        return render_template("edit.html", reference=reference)
    return redirect("/")