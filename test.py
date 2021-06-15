import unittest
import hello

class HelloTest(unittest.TestCase):

    def testHelloWorld(self):
        self.assertEqual(hello.helloWorld(), "Hello World!")