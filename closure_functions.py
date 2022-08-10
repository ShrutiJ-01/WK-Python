# Python program to illustrate
# nested functions
def outerFunction():
    text = 900
    def innerFunction():
        text = 200
        print(text)

    return innerFunction

ifn = outerFunction()
ifn()