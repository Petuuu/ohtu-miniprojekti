"""Unit tests for the Reference model"""

from dataclasses import asdict, fields
import unittest

from models.reference import Reference


class ReferenceTest(unittest.TestCase):
    def test_key_is_required(self):
        with self.assertRaises(TypeError):
            Reference() # pylint: disable=no-value-for-parameter

    def test_reference_uses_default_values_when_none(self):
        ref = Reference(key="abc")

        self.assertEqual(ref.key, "abc")
        self.assertEqual(ref.entry_type, "article")

    def test_reference_uses_default_values_when_empty(self):
        ref = Reference(key="abc", entry_type="")

        self.assertEqual(ref.key, "abc")
        self.assertEqual(ref.entry_type, "article")

    def test_optional_fields_default_to_none(self):
        ref = Reference(key="abc")

        for field in fields(Reference):
            if field.name in ("key", "entry_type"):
                continue
            with self.subTest(field=field.name):
                self.assertIsNone(getattr(ref, field.name))

    def test_given_values_stored(self):
        ref = Reference(
            key="abc",
            entry_type="book",
            author="Meikäläinen, Matti",
            title="Pythonin perusteet",
            year=1995
        )

        self.assertEqual(ref.entry_type, "book")
        self.assertEqual(ref.author, "Meikäläinen, Matti")
        self.assertEqual(ref.title, "Pythonin perusteet")
        self.assertEqual(ref.year, 1995)

    def test_getitem_returns_field_values(self):
        ref = Reference(
            key="abc",
            author="Meikäläinen, Matti",
            year=1995
        )

        self.assertEqual(ref["key"], "abc")
        self.assertEqual(ref["author"], "Meikäläinen, Matti")
        self.assertEqual(ref["year"], 1995)

    def test_getitem_returns_none_for_missing_field(self):
        ref = Reference(
            key="abc",
            author="Meikäläinen, Matti",
            year=1995
        )

        self.assertIsNone(ref["title"])
