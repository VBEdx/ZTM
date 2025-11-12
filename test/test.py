import unittest
import someCode

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_add_number(self):
        test_param=10
        result = someCode.add_number(test_param)
        self.assertEqual(result, 15)

    def test_add_number2(self):
        # test a string
        test_param='ten'
        result = someCode.add_number(test_param)
        self.assertIsInstance(result, ValueError)

    def test_add_number3(self):
        # test a string
        test_param=None
        result = someCode.add_number(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        print('clean up')

if __name__ == '__main__':
    unittest.main()



