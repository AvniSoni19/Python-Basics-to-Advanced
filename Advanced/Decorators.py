def hello(name='MediCaps'):
    return 'Welcome to '+name
print(hello())

welcome=hello
print(welcome())
del hello
#print(hello)

def new_decorator(func):

    def wrap_func():
        print('first')

        print('second')
        func()
    return wrap_func
def func_needs_decorator():
    print('third')

func_needs_decorator()
new_func=new_decorator(func_needs_decorator)
new_func()
print('\n')

@new_decorator#This is how you define a decorator
def func_need_decorator():
    print("Third")

func_need_decorator()