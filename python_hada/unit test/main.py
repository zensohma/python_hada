import unittest

class TestStringMethods(unittest.TestCase):
    # ini adalah case pertama
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    # test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    # test case ketiga
    def test_index(self):
        s = 'dicoding'
        self.assertEquals(s.index('coding'), 2)

        with self.assertRaises(ValueError):
            s.index('decode')


if __name__ == "__main__":
    # Test Runner
    unittest.main()
