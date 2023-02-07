class InputOutputString:         #1
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())


strObj = InputOutputString()
strObj.getString()
strObj.printString()

