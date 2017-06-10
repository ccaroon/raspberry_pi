import urlparse
import BaseHTTPServer

import server

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def __init__(self, request, client_address, svr):
        super(RequestHandler, self).__init__(request, client_address, svr)
        self.__action_handler = server.ActionHandler()

    def do_GET(self):
        url = urlparse.urlparse(self.path)
        qs = urlparse.parse_qs(url.query)
        success = self.__action_handler.handle(url.path, qs)

        self.send_header("Content-type", "text/plain")
        self.end_headers()

        if success:
            self.send_response(200)
            self.wfile.write("Processed %s" % (url.path))
        else:
            self.send_response(500)
            self.wfile.write("It's pitch black. You have been eaten by a Gru.\n")
