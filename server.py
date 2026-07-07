import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("RECEIVED ERROR:", post_data.decode('utf-8'))
        self.send_response(200)
        self.end_headers()

with socketserver.TCPServer(("", 8081), MyHandler) as httpd:
    httpd.serve_forever()
