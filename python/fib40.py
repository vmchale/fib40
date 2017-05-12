import socketserver
import http.server

PORT = 3000

def fibonacci (n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(fibonacci(40))
        return

httpd = socketserver.ThreadingTCPServer(('localhost', PORT),CustomHandler)

print("serving at port", PORT)
httpd.serve_forever()
