#create a function that use as a decorator
def  mydecorators(callback):
    print("This is my decorator")
    return callback
    
#initalize decorator
@mydecorators
def dosomething():
    print("hello")

dosomething()
