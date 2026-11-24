"""Provides operations for reference management."""

from models.reference import Reference
from repositories.reference_repository import ReferenceRepository


class ReferenceService:
    def __init__(self, repository: ReferenceRepository):
        self._repository = repository

    def create_reference(self, args):
        self.validate(args)
        self._repository.create_reference(Reference(**args))

    def get_references(self):
        return self._repository.get_references()

    def remove_reference(self, key):
        self._repository.remove_reference(key)

    def find_by_key(self, key):
        return self._repository.find_by_key(key)

    def validate(self, args):
        for key, value in args.items():
            if value:
                if key == "year" and int(value) > 2026 or int(value) < 0:
                    raise ValueError("year must not be negative or in the future")
                elif len(value) > 1000:
                    raise ValueError(f"{key} is too long (max 1000)")


reference_service = ReferenceService(ReferenceRepository())
