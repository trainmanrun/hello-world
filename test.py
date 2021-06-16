import hello
import sys

def testHelloWorld():
    retVal = 1
    if hello.helloWorld() == "Hello World!":
        print("Success!")
        retVal = 0
    else:
        print("Failure!")
        retval = 1
    sys.exit(retVal)

testHelloWorld()