import unittest
import gummybears

class TestGummyBears(unittest.TestCase):

    def test_gummybears(self):
        import gummybears
        self.assertEqual(gummybears.cli(), 'Hello there!')

if __name__ == '__main__':
    unittest.main()
