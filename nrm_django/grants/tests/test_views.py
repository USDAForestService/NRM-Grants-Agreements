import datetime
from django.utils import timezone

from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from grants.models import Grant
from django.contrib.auth import get_user_model

class GrantUpdateViewTest(TestCase):

	@classmethod
	def setUpTestData(klass):
		klass.grant = Grant.objects.create(
			cn='162219ddc3010602',
			app_submit_date=datetime.date.today(),
			app_received_date=datetime.date.today(),
			proposed_start_date=datetime.date.today(),
			proposed_end_date=datetime.date.today(),
			created_in_instance=0,
		)
		klass.grant_x = Grant.objects.create(
			cn='73010312X',
			app_submit_date=datetime.date.today(),
			app_received_date=datetime.date.today(),
			proposed_start_date=datetime.date.today(),
			proposed_end_date=datetime.date.today(),
			created_in_instance=0,
		)

		klass.grants = [klass.grant, klass.grant_x]

	def setUp(self):
		self.client = Client()
		self.user = get_user_model().objects.create_user('admin', 'admin@usda.gov', '')
		self.client.login(username='admin', password='')  # nosec

	def tearDown(self):
		self.user.delete()

	def test_redirect_if_not_logged_in(self):
		self.client.logout()
		response = self.client.get(f"/admin/grants/grant/{self.grant.pk}/change")
		self.assertRedirects(response, f"/admin/login/?next=/admin/grants/grant/{self.grant.pk}/change")

	def test_admin_login(self):
		"""Successfully visits /admin"""
		response = self.client.get('/admin', follow=True)
		self.assertEqual(response.status_code, 200)

	def test_logged_in_uses_correct_template(self):
		for grant in self.grants:
			response = self.client.get(f"/admin/grants/grant/{grant.pk}/change/", follow=True)

			self.assertEqual(response.status_code, 200)
			self.assertEqual(str(response.context['user']), 'admin')

			# Check we used correct template
			self.assertTemplateUsed(response, 'grants/update.html')



