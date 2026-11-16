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
