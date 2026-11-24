"""ReferenceRepository tests."""

import unittest
from unittest.mock import Mock

from sqlalchemy import Column, Integer, MetaData, String, Table

from models.reference import Reference
from repositories.reference_repository import ReferenceRepository


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        self.mock_session = Mock()
        self.metadata = MetaData()
        self.table = Table(
            "ReferenceTable",
            self.metadata,
            Column("key", String, primary_key=True),
            Column("title", String,),
            Column("author", String),
            Column("year", Integer),
            Column("entry_type", String),
        )

        self.repository = ReferenceRepository(
            session=self.mock_session,
            table=self.table,
        )

        self.test_reference = Reference(
            key="martin2008",
            entry_type="book",
            author="Robert C. Martin",
            title="Clean Code",
            year=2008,
        )

    def test_create_reference_executes_statements_and_commits(self):
        self.repository.create_reference(self.test_reference)

        self.mock_session.execute.assert_called_once()
        self.mock_session.commit.assert_called_once()

    def test_get_references_empty_when_no_rows(self):
        self.mock_session.execute.return_value.all.return_value = []

        result = self.repository.get_references()

        self.assertEqual(result, [])

        self.mock_session.execute.assert_called_once()

    def test_get_references_returns_mapped_reference_objects(self):
        mock_row = Mock()
        mock_row._asdict.return_value = {
            "key": "martin2008",
            "entry_type": "book",
            "author": "Robert C. Martin",
            "title": "Clean Code",
            "year": 2008,
        }
        self.mock_session.execute.return_value.all.return_value = [mock_row]

        references = self.repository.get_references()

        self.assertEqual(len(references), 1)
        self.assertIsInstance(references[0], Reference)
        self.assertEqual(references[0]. key, "martin2008")
        self.assertEqual(references[0].title, "Clean Code")

    def test_find_by_key_returns_reference_when_found(self):
        mock_row = Mock()
        mock_row._asdict.return_value = {
            "key": "martin2008",
            "entry_type": "book",
            "author": "Robert C. Martin",
            "title": "Clean Code",
            "year": 2008,
        }
        self.mock_session.execute.return_value.first.return_value = mock_row

        found = self.repository.find_by_key("martin2008")

        self.assertIsNotNone(found)
        self.assertEqual(found.key, "martin2008")
        self.mock_session.execute.assert_called_once()

    def test_find_by_key_returns_none_when_not_found(self):
        self.mock_session.execute.return_value.first.return_value = None

        found = self.repository.find_by_key("nonexistent")

        self.assertIsNone(found)
        self.mock_session.execute.assert_called_once()

    def test_remove_reference_deletes_and_commits_when_found(self):
        mock_row = Mock()
        mock_row._asdict.return_value = {
            "key": "martin2008",
            "entry_type": "book",
            "author": "Robert C. Martin",
            "title": "Clean Code",
            "year": 2008,
        }
        self.mock_session.execute.return_value.first.return_value = mock_row

        self.repository.remove_reference("martin2008")

        self.assertEqual(self.mock_session.execute.call_count, 2)
        self.mock_session.commit.assert_called_once()

    def test_remove_reference_raises_key_error_and_does_not_commit_when_not_found(self):
        self.mock_session.execute.return_value.first.return_value = None

        with self.assertRaises(KeyError):
            self.repository.remove_reference("nonexistent")

        self.mock_session.commit.assert_not_called()
