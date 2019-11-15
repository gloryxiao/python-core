#!/usr/bin/python
# coding=utf-8

# 222.173.10.82 8888 可用代理

import requests
import traceback


def main():
    test_url = "https://www.baidu.com"
    test_proxy_list = [("222.173.10.82", "8888"), ("171.12.138.121", "36018")]
    try:
        for item in test_proxy_list:
            host = item[0]
            port = item[1]
            proxy_addr = host + ":" + port
            proxy = {"http": "http://" + proxy_addr,
                     "https": "https://" + proxy_addr,
                     }
            r = requests.get(test_url,
                             proxies=proxy,
                             timeout=2,
                             verify=False
                             )
            if r.status_code == 200:
                print "get succ, with %s" % proxy
            else:
                print r

    except Exception as e:
        print traceback.format_exc(e)


if __name__ == "__main__":
    main()
