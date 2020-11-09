import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(check_pwd('Abcd1234@'))

    def test2(self):
        self.assertFalse(check_pwd('Abcd12@'))

    def test3(self):
        self.assertFalse(check_pwd('Abcdefg1234566789505990329@@'))

    def test4(self):
        self.assertFalse(check_pwd('abcd1234@'))

    def test5(self):
        self.assertFalse(check_pwd('ABCD1234@'))

    def test6(self):
        self.assertFalse(check_pwd('ABCDabcd@'))

    def test7(self):
        self.assertFalse(check_pwd('Abcd1234'))


if __name__ == '__main__':
    unittest.main()
