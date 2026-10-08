from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello World from Docker!</h1><p>SWE40006 Task 4.2 - Python web server</p>")

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()