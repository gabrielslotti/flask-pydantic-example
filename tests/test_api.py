from unittest import TestCase
from pydantic import ValidationError
from parameterized import parameterized

from app import app


class TestAPI(TestCase):
    @parameterized.expand([('test'), ('test2')])
    def test_get_name_ok(self, input):
        res = app.test_client().get(f'/name/{input}')
        self.assertEqual(res.status_code, 200)

    @parameterized.expand([(1), ('2')])
    def test_get_number_ok(self, input):
        res = app.test_client().get(f'/number/{input}')
        self.assertEqual(res.status_code, 200)

    @parameterized.expand([('test'), ('test2')])
    def test_get_number_err(self, input):
        res = app.test_client().get(f'/number/{input}')
        self.assertEqual(res.status_code, 400)
        assert 'validation_error' in res.json