import http.server
import socketserver
from urllib.parse import quote

PORT = 8080
FILENAME = "programme_équation du second degré.py"

Handler = http.server.SimpleHTTPRequestHandler

class MyHandler(Handler):
    def translate_path(self, path):
        # Utilisez quote pour encoder le nom du fichier
        return super().translate_path(quote(path, safe="/~!*()"))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()