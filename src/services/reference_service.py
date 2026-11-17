from src.models.article import Article
from src.repositories.reference_repository import ReferenceRepository


class ReferenceService:
    def __init__(self, repository):
        self._repository = repository

    def create_reference(self, **args):
        self.validate(**args)
        self._repository.create_reference(Article(**args))

    def validate(self):
        pass
