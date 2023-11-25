import unittest
from modules.load_settings import load_ini
from pathlib import Path


class TestLoadSettings(unittest.TestCase):
    def test_load_ini(self):
        expected = {
            'api_token': '[GET_TOKEN_FROM_SWITCHBOT_APP]',
            'api_secret': '[GET_CLIENT_SECRET_FROM_SWITCHBOT_APP]'
        }
        p = Path(__file__).parent.parent / 'settings.ini.template'
        actual = load_ini(p.as_posix())
        self.assertEqual(actual, expected)
