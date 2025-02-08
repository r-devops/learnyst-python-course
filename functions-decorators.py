def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


def formatter(func):
    def wrapper():
        print("****************************************************")
        func()
        print("****************************************************")
    return wrapper

@formatter
def say_hello():
    print("Hello!")

say_hello()



def repeat(func):
    def wrapper(name):
        for _ in range(3):
            result = func(name)
        return result
    return wrapper

@repeat
def greet(name):
    print(f"Hello {name}")

greet("Alice")


# Built-in Decorators

class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")

    @classmethod
    def my_class_method(cls):
        print(f"This is a class method.")

    @property
    def my_property(self):
        return "This is a property."

obj = MyClass()
obj.my_static_method()
obj.my_class_method()
print(obj.my_property)


