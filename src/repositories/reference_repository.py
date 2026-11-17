from models.reference import Reference


class ReferenceRepository:
    def __init__(self):
        self._list = []

    def create_reference(self, reference: Reference):
        self._list.append(reference)

    def get_references(self):
        return self._list
