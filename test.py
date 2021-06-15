import hello

def testHelloWorld():
    if hello.helloWorld() == "Hello World!":
    	print("Success!");
        return 0
    else:
        print("Failure!")
        return 1

testHelloWorld()