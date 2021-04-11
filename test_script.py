import unittest
import proga


class TestMain(unittest.TestCase):
    def setUp(self):
        print('Test begining')

    def test_my_sum(self):
        test_param = 10
        result = proga.my_sum(test_param)
        self.assertEqual(result, 15)

    def test_my_sum1(self):
        test_param = 'testing'
        result = proga.my_sum(test_param)
        self.assertIsInstance(result,TypeError)

    def test_my_sum2(self):
        test_param = None
        result = proga.my_sum(test_param)
        self.assertEqual(result, "Enter a Value")

    def tearDown(self):
        print('cleaning up')
