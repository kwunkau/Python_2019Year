# args用法，多个值
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


# kwargs用法，**kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("%s =+_+= %s" % (key, value))
        print("{} =+_+= {}".format(key, value))  # 占位符两种表现形式


greet_me(name="apple")


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# 首先使用 *args
args = ("two", 3, 5)
test_args_kwargs(*args)

# 现在使用 **kwargs:
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
