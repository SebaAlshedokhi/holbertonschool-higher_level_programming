#!/usr/bin/python3
"""RESTful API"""
import http.server
import socketserver
import json

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    """
    class for handling server requests
    """
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"A simple API!")
            
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not found")

Handler = MyHandler
with socketserver.TCPServer(("", PORT), Handler) as httppp:
    print(f"Serving at port {PORT}")
    httppp.serve_forever()
