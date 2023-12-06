import unittest
from DataCapture import DataCapture


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.capture = DataCapture()

        self.capture.add(3)
        self.capture.add(9)
        self.capture.add(3)
        self.capture.add(4)
        self.capture.add(6)

        self.stats = self.capture.build_stats()

    def test_less(self):
        result = self.stats.less(4)

        self.assertEqual(result, [3, 3])

    def test_less_on_left_edge(self):
        result = self.stats.less(9)

        self.assertEqual(result, [3, 3, 4, 6])

    def test_less_on_right_edge(self):
        result = self.stats.less(3)

        self.assertEqual(result, [])

    def test_between(self):
        result = self.stats.between(3, 6)

        self.assertEqual(result, [3, 3, 4, 6])

    def test_between_on_edge(self):
        result = self.stats.between(3, 9)

        self.assertEqual(result, [3, 3, 4, 6, 9])

    def test_greater(self):
        result = self.stats.greater(4)

        self.assertEqual(result, [6, 9])

    def test_greater_on_right_edge(self):
        result = self.stats.greater(9)

        self.assertEqual(result, [])

    def test_greater_on_left_edge(self):
        result = self.stats.greater(3)

        self.assertEqual(result, [4, 6, 9])


if __name__ == '__main__':
    unittest.main()
