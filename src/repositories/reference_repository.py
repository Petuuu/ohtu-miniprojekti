"""Stores references in memory."""

from models.reference import Reference


class ReferenceRepository:
    def __init__(self):
        self._list = []

    def create_reference(self, reference: Reference):
        self._list.append(reference)

    def get_references(self):
        return self._list

    def find_by_key(self, key):
        for ref in self._list:
            if ref.key == key:
                return ref
        return None

    def remove_reference(self, key: str):
        reference = self.find_by_key(key)
        if reference is None:
            raise KeyError(f"Reference with key '{key}' cannot be found")
        self._list.remove(reference)
