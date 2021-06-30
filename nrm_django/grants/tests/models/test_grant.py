from django.test import TestCase
from grants.models import Grant

class GrantTestCase(TestCase):
    def test_something(self):
        subject = Grant(
            cn=1,
            proj_title = "Project Title",
        )
        self.assertTrue(subject)
