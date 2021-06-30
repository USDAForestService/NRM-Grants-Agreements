from django.test import TestCase
from grants.models import Note

class NoteTestCase(TestCase):
    def test_something(self):
        subject = Note(
            cn=1,
        )
        self.assertTrue(subject)
