from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #  Mock Auth checker
        print("Mocking auth decorator")
        return func(*args, **kwargs)

    return wrapper
