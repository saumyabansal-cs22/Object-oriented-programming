# def hello():
#     print("hello world!")
def greet(fx):
    def mfx(*a,**d):
        print("hello hi")
        fx(*a,**d)
        print("this is a decorator tutorial")
    return mfx
# greet(hello)()
@greet
def hello():
    print("hello world!")
hello()
def add(a,b):
    print(a+b)
greet(add)(1,2)