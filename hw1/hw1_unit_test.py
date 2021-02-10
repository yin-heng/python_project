import unittest
import HW1

class TestHW1(unittest.TestCase):

    def setUp(self):
        self.operations = HW1.Operations()

    def tearDown(self):
        self.operations = None

    def test_1(self):
        self.operations.write('Hello world')
        self.operations.read()
        self.operations.status()
        self.operations.write_to_offset(int(11),'! This is a test')
        self.assertEqual(self.operations.read().replace(b'\x00', b'').decode('utf-8'), 'Hello world! This is a test')

    def test_2(self):
        self.operations.write('Today has been a bland day')
        self.operations.read()
        self.operations.status()
        self.operations.write_to_offset(int(17),'great')
        self.assertEqual(self.operations.read().replace(b'\x00', b'').decode('utf-8'), 'Today has been a great day')

    def test_exception(self):
        self.operations.write('Hello world')
        self.operations.read()
        self.operations.status()
        self.assertRaises(Exception, "offset to write is invalid", self.operations.write_to_offset, int(17),'! This is a test')

if __name__ == '__main__':
    unittest.main()