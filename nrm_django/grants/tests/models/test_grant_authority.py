from django.test import TestCase
from grants.models import GrantAuthority


class GrantAuthorityTestCase(TestCase):
    def test_creation(self):
        subject = GrantAuthority(
            pk=1,
        )
        self.assertTrue(subject)
