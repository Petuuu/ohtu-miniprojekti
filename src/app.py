"""Defines the Flask routes for the application."""

from flask import flash, redirect, render_template, request

from config import app
from services.reference_service import reference_service


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
