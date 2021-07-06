from django.test import TestCase
from grants.models import Note


class NoteTestCase(TestCase):
    def test_creation(self):
        subject = Note(
            cn=1,
        )
        self.assertTrue(subject)
