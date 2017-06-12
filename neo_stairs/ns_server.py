#!/usr/bin/env python
import BaseHTTPServer
import server

if __name__ == '__main__':

    PORT = 8000

    httpd = BaseHTTPServer.HTTPServer(("", PORT), server.RequestHandler)
    try:
        print "NeoStairs Server starting on port: ", PORT
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print "NeoStaris Server stopping."
