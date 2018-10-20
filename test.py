import unittest
import code

class Test(unittest.TestCase):

    def testCode1(self):
        self.assertEqual(code.code(1), 2)
        
    def testCode2(self):
        self.assertEqual(code.code(2), 4)
        
    def testCode3(self):
        self.assertEqual(code.code(3), 6)
        
    def testCode4(self):
        self.assertEqual(code.code(4), 8)
        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()