"""Provides operations for reference management."""

from datetime import datetime
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

    def validate(self, args):
        for key, value in args.items():
            if value:
                if key == "year":
                    try:
                        year = int(value)
                    except Exception as exc:
                        raise ValueError("year must be integer") from exc

                    if year > datetime.now().year or int(value) < 0:
                        raise ValueError("year must not be negative or in the future")

                if len(value) > 1000:
                    raise ValueError(f"{key} is too long (max 1000)")


reference_service = ReferenceService(ReferenceRepository())
