from dataclasses import dataclass
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

    def __init__(self, author, title, journal = None, year = None, volume = None, number = None, pages = None, month = None, note = None):
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.number = number
        self.pages = pages
        self.month = month
        self.note = note
        self._list = [self.author, self.title, self.journal, self.year, self.volume, self.number, self.pages, self.month, self.note]

    def __iter__(self):
        return iter(self._list)

    def __getitem__(self, index):
        if index > 0 and index < len(self._list):
            return self._list[index]
        else:
            raise IndexError