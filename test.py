import unittest
import ccwc


class MyTestCase(unittest.TestCase):
    def test_bytes(self):
        self.assertEqual(ccwc.get_file_bytes('test.txt'), 342190)

    def test_lines(self):
        self.assertEqual(ccwc.get_file_lines('test.txt'), 7145)

    def test_chars(self):
        self.assertEqual(ccwc.get_file_chars('test.txt'), 339292)

    def test_words(self):
        self.assertEqual(ccwc.get_file_words('test.txt'), 58164)

    def test_all(self):
        self.assertEqual(ccwc.calculate_all('test.txt'), (339292, 58164, 7145, 342190))


if __name__ == '__main__':
    unittest.main()
