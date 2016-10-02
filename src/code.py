#!/usr/bin/env python
# coding=utf-8

import web #import the package for web

urls =  ("/", "index", "/test*", "test")
def readhtml(htmlfile):
    return open(htmlfile, 'rb').read()

class index:
    def GET(self):
        return readhtml("index.html")
        
class test():
    def GET(self):
        user_data = web.input()
        fisrt_name = user_data.FirstName
        last_name = user_data.LastName
        return "<h1>Your input name:</h1><h3><font color='blue'> %s %s</font></h3>"\
                % (fisrt_name, last_name)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
