import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

class MyWebsiteHandler(SimpleHTTPRequestHandler):
    # This overrides the default behavior only for the root URL "/"
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        # Python handles the reading, opening, and serving the files safely.
        return super().do_GET()

if __name__ == "__main__":
    # Ensure the server runs out of the directory where this script lives
    web_dir = os.path.dirname(__file__)
    if web_dir:
        os.chdir(web_dir)

    server = ThreadingHTTPServer(("127.0.0.1", 8000), MyWebsiteHandler)
    print("Server running on http://127.0.0.1:8000 ...")
    server.serve_forever()
