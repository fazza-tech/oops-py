
def announce(f):
    def wrapper():
        print("about to run the program...")
        f()
        print("done with the programe")
    return wrapper
    

@announce
def hello():
    print("Hello world")

hello()

