def limit_povernenya(a, b):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result = a if result < a else b
            return result
        return wrapper
    return decorator

@limit_povernenya(0, 1)
def f(x):
    return x * 2 - 1

result = f(3)
print(result)