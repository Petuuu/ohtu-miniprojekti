from dataclasses import dataclass


@dataclass
class Reference:
    """Data Class for an Reference."""

    key: str
    entry_type: str
    address: str | None = None
    annote: str | None = None
    author: str | None = None
    booktitle: str | None = None
    chapter: str | None = None
    crossref: str | None = None
    doi: str | None = None
    edition: str | None = None
    editor: str | None = None
    email: str | None = None
    eprint: str | None = None
    howpublished: str | None = None
    institution: str | None = None
    isbn: str | None = None
    issn: str | None = None
    journal: str | None = None
    month: str | None = None
    note: str | None = None
    number: str | None = None
    organization: str | None = None
    pages: str | None = None
    publisher: str | None = None
    school: str | None = None
    series: str | None = None
    title: str | None = None
    type: str | None = None
    url: str | None = None
    volume: str | None = None
    year: int | None = None
    zblnumber: str | None = None

    def __post_init__(self):
        self._dict = {
            "key": self.key,
            "entry_type": self.entry_type,
            "address": self.address,
            "annote": self.annote,
            "author": self.author,
            "booktitle": self.booktitle,
            "chapter": self.chapter,
            "crossref": self.crossref,
            "doi": self.doi,
            "edition": self.edition,
            "editor": self.editor,
            "email": self.email,
            "eprint": self.eprint,
            "howpublished": self.howpublished,
            "institution": self.institution,
            "isbn": self.isbn,
            "issn": self.issn,
            "journal": self.journal,
            "month": self.month,
            "note": self.note,
            "number": self.number,
            "organization": self.organization,
            "pages": self.pages,
            "publisher": self.publisher,
            "school": self.school,
            "series": self.series,
            "title": self.title,
            "type": self.type,
            "url": self.url,
            "volume": self.volume,
            "year": self.year,
            "zblnumber": self.zblnumber,
        }

    def __iter__(self):
        return iter(self._dict)

    def __getitem__(self, key):
        return self._dict[key]
