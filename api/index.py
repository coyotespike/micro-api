from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','json/application')
        self.end_headers()
        response = {
            "message": "Hello, World!",
            "location": "AWS Lambda"
        }
        self.wfile.write(bytes(json.dumps(response), "utf8"))
        return
