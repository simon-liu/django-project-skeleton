import unittest

from rest_framework.test import APIClient

from common.const import ErrorCode


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.client = APIClient()

    def assertResponseOK(self, response, status=None):
        if status is None:
            if not 200 <= response.status_code < 300:
                print(response.status_code, response.content)

            self.assertTrue(200 <= response.status_code < 300)
        else:
            if response.status_code != status:
                print(response.status_code, response.content)

            self.assertEqual(response.status_code, status)
            self.assertEqual(response.json()['code'], ErrorCode.OK)

    def assertResponseError(self, response, status_code, error_code):
        self.assertEqual(response.status_code, status_code)

        v = response.json()
        self.assertEqual(v['code'], error_code)
        self.assertEqual(v['message'], ErrorCode.message(error_code))
