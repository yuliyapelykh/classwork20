def result_over_zero(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 0:
            result = 1
        return result
    return wrapper

#функція
@result_over_zero
def f(x):
    return x * 2 - 1

result = f(3)
print(result)