from django.test import TestCase
from grants.models import GrantAuthority

class GrantAuthorityTestCase(TestCase):
    def test_something(self):
        subject = GrantAuthority(
            pk=1,
        )
        self.assertTrue(subject)
