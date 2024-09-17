import program
import unittest

class TestSum(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(program.add(5, 5), 10)

if __name__ == '__main__':
    unittest.main()