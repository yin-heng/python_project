import unittest
import HW1

operations = None

class TestHW1(unittest.TestCase):

    def setUp(self):
        operations = HW1.Operations()

    def tearDown(self):
        operations = None

    def test_1(self):
        operations = HW1.Operations()
        operations.write('Hello world')
        operations.read()
        operations.status()
        operations.write_to_offset(int(11),'! This is a test')
        self.assertEqual(operations.read().replace(b'\x00', b'').decode('utf-8'), 'Hello world! This is a test')

    def test_2(self):
        operations = HW1.Operations()
        operations.write('Today has been a bland day')
        operations.read()
        operations.status()
        operations.write_to_offset(int(17),'great')
        self.assertEqual(operations.read().replace(b'\x00', b'').decode('utf-8'), 'Today has been a great day')

    def test_exception(self):
        operations = HW1.Operations()
        operations.write('Hello world')
        operations.read()
        operations.status()
        self.assertRaises(Exception, "offset to write is invalid", operations.write_to_offset, int(17),'! This is a test')

if __name__ == '__main__':
    unittest.main()