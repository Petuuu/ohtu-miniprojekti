from dataclasses import dataclass
from dataclasses import field

from .reference import Reference


@dataclass
class Article(Reference):
    """Data Class for an article."""

    author: str | None = None
    title: str | None = None
    journal: str | None = None
    year: int | None = None
    volume: int | None = None
    number: int | None = None
    pages: str | None = None
    month: str | None = None
    note: str | None = None

    def __post_init__(self):
        self._list = [
            self.author,
            self.title,
            self.journal,
            self.year,
            self.volume,
            self.number,
            self.pages,
            self.month,
            self.note,
        ]
        self._dict = {"author": self.author, "title": self.title, "journal" : self.journal, "year": self.year,
                       "volume":self.volume, "number" : self.number, "pages": self.pages, "month" : self.month,
                        "note": self.note}
    def __iter__(self):
        return iter(self._list)

    def __getitem__(self, index):
        if index >= 0 and index < len(self._list):
            return self._list[index]
        else:
            raise IndexError
