def check(func):
    def inner_wrapper(arg):
        res = func(arg)
        print("we have done some work iside decorator")
        return res
    return inner_wrapper

@check
def foo(a):
    return f'moo - {a}'

print(foo(123))