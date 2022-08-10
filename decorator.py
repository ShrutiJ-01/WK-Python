import datetime

def timed_greeting(func):
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        func("My","name","is","Shruti")
        print("\nThis is a rainy day")

@timed_greeting
def greeting(*args):
    print("Hello")
    for arg in args:
        print(f"{arg}", end=" ")