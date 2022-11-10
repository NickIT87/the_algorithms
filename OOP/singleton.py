class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=MetaSingleton):
    a = "Test"

    def get_a(self):
        return self.a


new_a = MyClass()
new_b = MyClass()

print(new_a.get_a())
print(new_b.get_a())