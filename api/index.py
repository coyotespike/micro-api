from http.server import BaseHTTPRequestHandler
import json

from .db_access import find_embeddings

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # find_embeddings()
        self.send_response(200)
        # self.send_header('Content-type','json/application')
        self.send_header('Content-type','text/html')
        self.end_headers()
        response = {
            "message": "Hello, World!",
            "location": "AWS Lambda"
        }
        # self.wfile.write(bytes(json.dumps(response), "utf8"))
        self.wfile.write(bytes("Hello, World!", "utf8"))
        return
