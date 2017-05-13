import socketserver
import http.server

PORT = 3000

def fib_memo(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fib_memo(n-1) + fib_memo(n-2))
    return 1

def fib(n):
    x = [1,1]
    for i in range(n):    
        x.append(x[-1] + x[-2])

def fib_naive (n):
    if n < 2:
        return 1
    else:
        return fib_naive(n - 2) + fib_naive(n - 1)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write((str(fib_naive(40)) + '\n').encode())
        return

httpd = socketserver.ThreadingTCPServer(('localhost', PORT),CustomHandler)

print("serving at port", PORT)
httpd.serve_forever()
