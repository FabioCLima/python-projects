class ClassTest:

    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


test = ClassTest()
test.instance_method()
ClassTest.class_method()
test.static_method()
