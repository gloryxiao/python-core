#!/usr/bin/env python
# coding=utf-8

# python3语法会将上层的异常信息捕获，并有能力传递给后面的异常
if __name__ == "__main__":
    try:
        raise IOError("not found io file")
    except IOError as ex:
        raise Exception("haha") from ex
