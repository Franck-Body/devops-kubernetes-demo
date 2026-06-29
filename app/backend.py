from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from backend service")

server = HTTPServer(("0.0.0.0", 9000), Handler)
print("Backend running on port 9000")
server.serve_forever()
