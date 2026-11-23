"""Provides operations for reference management."""

from models.article import Article
from repositories.reference_repository import ReferenceRepository


class ReferenceService:
    def __init__(self, repository: ReferenceRepository):
        self._repository = repository

    def create_reference(self, *args):
        self.validate(*args)
        self._repository.create_reference(Article(*args))

    def get_references(self):
        return self._repository.get_references()

    def remove_reference(self, key):
        self._repository.remove_reference(key)

    def validate(self, *args):
        for arg in args:
            if len(arg) >= 150:
                raise ValueError


reference_service = ReferenceService(ReferenceRepository())
