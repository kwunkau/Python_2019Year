import time


def deco(func):
    def wrapper():
        start_time = time.time()
        func()  # return可用可不用
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print("time is %d ms" % execution_time)
        return func()  # 尾部重新调用一次

    return wrapper


@deco
def f():
    print("hello")
    time.sleep(1)
    print("world")


if __name__ == '__main__':
    f()
