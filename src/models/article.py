from dataclasses import dataclass
from dataclasses import field

from src.models.reference import Reference

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
    _list: list[str | int | None] = field(init=False, repr=False)

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

    def __iter__(self):
        return iter(self._list)

    def __getitem__(self, index):
        if index >= 0 and index < len(self._list):
            return self._list[index]
        else:
            raise IndexError
