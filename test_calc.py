import unittest
import calc


class TestBoundedBox(unittest.TestCase):
    def test_bounded_box(self):
        self.assertListEqual(calc.get_bounded_box("AMS"), [51.30751991891892, 53.309682081081085, 3.153455217391297,
                                                           6.37432478260871])
        self.assertEqual(calc.get_bounded_box("LAX"), [32.94141991891892, 34.94358208108108, -120.01843178260869,
                                                       -116.7975622173913])


if __name__ == "__main__":
    unittest.main()
