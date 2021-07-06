from django.test import TestCase
from grants.models import Category


class CategoryTestCase(TestCase):
    def test_creation(self):
        subject = Category(
            cn=1,
        )
        self.assertTrue(subject)
