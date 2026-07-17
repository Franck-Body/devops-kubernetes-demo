import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys

app_mode = os.getenv("APP_MODE", "dev")
log_level = os.getenv("LOG_LEVEL")
database_password = os.getenv("DATABASE_PASSWORD")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        if database_password:
            password_status = "Password loaded successfully"
        else:
            password_status = "Password NOT loaded"

        response = (
            f"Hello DevOps\n"
            f"Mode: {app_mode}\n"
            f"Log level: {log_level}\n"
            f"{password_status}"
        )

        self.wfile.write(response.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)

def shutdown_handler(signal_received, frame):
    print("Shutdown signal received")
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)

server.serve_forever()
