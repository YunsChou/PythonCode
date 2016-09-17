#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

from helloflask import app as application

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    print('localhost:8051')
    httpd.handle_request()


