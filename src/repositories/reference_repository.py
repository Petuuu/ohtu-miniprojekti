"""Stores references in database."""

from sqlalchemy import Table, delete, insert, select

from config import db
from models.reference import Reference


class ReferenceRepository:
    def __init__(self, session=None, table=None):
        self.session = session or db.session
        self._table = table

    @property
    def table(self):
        if self._table is None:
            self._table = Table("ReferencesTable", db.metadata, autoload_with=db.engine)
        return self._table

    def create_reference(self, reference: Reference) -> None:
        """Saves a reference using insert().values(...)."""
        values = {
            col.name: getattr(reference, col.name)
            for col in self.table.columns
            if hasattr(reference, col.name)
        }

        stmt = insert(self.table).values(values)
        self.session.execute(stmt)
        self.session.commit()

    def get_references(self) -> list[Reference]:
        """Retrieves all references using select()."""
        stmt = select(self.table)
        rows = self.session.execute(stmt).all()

        return [Reference(**row._asdict()) for row in rows]

    def find_by_key(self, key: str) -> Reference | None:
        """Retrieves a single reference using select().where()."""
        stmt = select(self.table).where(self.table.c.key == key)
        row = self.session.execute(stmt).first()

        return Reference(**row._asdict()) if row else None

    def remove_reference(self, key: str) -> None:
        """Deletes a reference using delete().where()."""
        reference = self.find_by_key(key)
        if reference is None:
            raise KeyError(f"Reference with key '{key}' cannot be found")

        stmt = delete(self.table).where(self.table.c.key == key)
        self.session.execute(stmt)
        self.session.commit()
