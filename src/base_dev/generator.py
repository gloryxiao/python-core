#!/usr/bin/env python
# coding=utf-8


def fab(n):
    if n <= 1:
        return                         # python3.3以前不允许生成器return 带参数
        # return None                  # 语法error

    x, y = 1, 1
    step = 1
    while step <= n:
        try:                           # try except 包含yield也没有问题
            yield x
            tmp = x
            x = y
            y += tmp
            step += 1
            if x > 100:
                # raise Exception("too big count")
                return
        except Exception as e:
            print e.message
            # raise e

        # try:                          # try except 语句不包含yield逻辑是OK的，没有语法问题
        #     raise Exception(u"aa")
        # except Exception as e:
        #     pass


if __name__ == "__main__":
    f = fab(-20)
    print f
    for item in f:
        print item

    f1 = (x+1 for x in xrange(100))
    print f1
    print dir(f1)
    f2 = xrange(10)
    print f2
    print type(f2), type(type(f2))
    print dir(f2)


