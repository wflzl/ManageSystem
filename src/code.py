#!/usr/bin/env python
# coding=utf-8

import web #import the package for web

urls =  ("/", "index", "/test*", "test")
render = web.template.render('templates')
def readhtml(htmlfile):
    # read html file to string
    return open(htmlfile, 'rb').read()

class index:
    def GET(self):
        return readhtml("index.html")
        
class test():
    def GET(self):
        # get the input of user in html
        user_data = web.input()
        fisrt_name = user_data.FirstName
        last_name = user_data.LastName
        return render.greeting(fisrt_name, last_name)
        #return "<h1>Your input name:</h1><h3><font color='blue'> %s %s</font></h3>"\
        #        % (fisrt_name, last_name)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
