import program
import unittest

class TestSum(unittest.TestCase):
    def test_negative_numbers(self):
        result = program.add(-3, -7)
        self.assertEqual(result, -10)

if __name__ == '__main__':
    unittest.main()

