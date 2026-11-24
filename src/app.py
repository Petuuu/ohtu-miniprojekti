"""Defines the Flask routes for the application."""

from flask import flash, redirect, render_template, request

from config import app
from services.reference_service import reference_service

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


@app.route("/")
def index():
    references = reference_service.get_references()
    return render_template("index.html", references=references)


@app.route("/add_reference", methods=["POST"])
def add_reference():
    args = {}
    for key in keys:
        args[key] = request.form.get(key)
    if not args.get("entry_type"):
        args["entry_type"] = "article"

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
    if request.method == "POST":
        args = {}
        for _key in keys:
            args[_key] = request.form.get(_key)
        if args["key"] != key and reference_service.find_by_key(args["key"]):
            flash("key was already taken")
            return redirect(f"/{key}/edit")
        try:
            reference_service.validate(args)
            reference_service.remove_reference(key)
            reference_service.create_reference(args)
        except ValueError:
            flash("Input was too long")

    return redirect("/")

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", debug=True)
