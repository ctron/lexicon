# Test for one implementation of the interface
from lexicon.providers.linode4 import Provider
from integration_tests import IntegrationTests
from unittest import TestCase
import pytest

# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests
class Linode4ProviderTests(TestCase, IntegrationTests):

	Provider = Provider
	provider_name = 'linode4'
	domain = 'lexicon-test.com'
	def _filter_post_data_parameters(self):
		return []

	def _filter_headers(self):
		return ['Authorization']

	def _filter_query_parameters(self):
		return []

	@pytest.mark.skip(reason="can not set ttl when creating/updating records")
	def test_Provider_when_calling_list_records_after_setting_ttl(self):
		return
