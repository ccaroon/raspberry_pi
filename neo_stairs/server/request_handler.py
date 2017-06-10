import urlparse
import BaseHTTPServer

import server

# Inherit from "object" so that I can use super() in __init__
class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler, object):

    def __init__(self, request, client_address, svr):
        self.__action_handler = server.ActionHandler()
        super(RequestHandler, self).__init__(request, client_address, svr)

    def do_GET(self):
        url = urlparse.urlparse(self.path)
        qs = urlparse.parse_qs(url.query)
        success = self.__action_handler.handle(url.path, qs)

        if success:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Processed %s\n" % (url.path))
        else:
            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("It's pitch black. You have been eaten by a Gru.\n")
