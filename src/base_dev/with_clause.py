#!/user/bin/env python
# coding=utf-8

import traceback


class func(object):
    def __enter__(self):
        # raise Exception("haha")
        pass

    def __exit__(self, type, value, trace):
        print type
        print value
        print trace
        print traceback.format_exc(trace)
        # return True       # 使用返回值True捕获with中抛出的不同的异常，异常不会抛出with上下文
        return 1            # 同上
        # return 0          # 使用返回值False(0)抛出异常，异常会抛出with上下文


if __name__ == "__main__":
    a = None
    with func() as f:
        raise Exception("bbb")
        a = 1

    print a


