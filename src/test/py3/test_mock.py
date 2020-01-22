#!/usr/bin/env python
# coding=utf-8

from unittest.mock import MagicMock, Mock, patch
from src.test.py2.widget import Widget


def main():
    def _mock(w):
        # mock method
        w.resize = MagicMock(return_value=3)
        # 返回3，无论传入参数
        print(w.resize(1, 2, 3, h=1))

    w = Widget("test")
    _mock(w)
    print(w.resize(1, 2, 3, h=1))

    # AssertionError
    try:
        w.resize.assert_called_with(1, 2, h=1)
    except AssertionError as ignore:
        print(ignore)

    # ok
    w.resize.assert_called_with(1,2,3,h=1)

    # side_effect属性
    i_mock = Mock(side_effect=Exception("side"))
    try:
        i_mock()
    except Exception as e:
        print(e)

    # 使用iterable对象或者函数
    i_mock.side_effect = [1,3,4]
    print(i_mock(), i_mock(), i_mock())

    i_mock.side_effect = lambda x=1: x
    print(i_mock(), i_mock(1000))


@patch("unittest.mock.Mock")
@patch("unittest.mock.MagicMock")
def test(ArgClass1, ArgClass2):
    Mock()
    MagicMock()
    assert ArgClass2 is Mock
    assert ArgClass1 is MagicMock
    assert ArgClass1.called
    assert ArgClass2.called


if __name__ == "__main__":
    main()
    test()

