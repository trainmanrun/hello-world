import unittest


class HelloTest(unittest.TestCase):

    def testHelloWorld(self):
        self.assertEqual(hello.helloWorld(), "Hello World!")