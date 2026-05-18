import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

MESSAGE = os.getenv("APP_MESSAGE", "Default message")

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(MESSAGE.encode())

PORT = 8000

server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"Server running on port {PORT}")
server.serve_forever()
