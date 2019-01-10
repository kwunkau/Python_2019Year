class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():  # 在静态方法中调用静态方法
        print("在静态方法中调用静态方法")
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):  # 在类方法中使用静态方法
        print("在类方法中使用静态方法")
        return cls.averag(cls.X, cls.Y)


foo = Foo()
print(foo.static_method())   #把自己作为参数传入方法
print(foo.class_method())
