import os
from sys import exit
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

class MyWebsiteHandler(SimpleHTTPRequestHandler):
    # This overrides the default behavior only for the root URL "/"
    # The file will be found based on the uri path
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        # Python handles the reading, opening, and serving the files safely.
        return super().do_GET()

if __name__ == "__main__":
    # Ensure the server runs out of the directory where this script lives
    web_dir = os.path.dirname(__file__)
    public_dir = os.path.join(web_dir, "website")
    if os.path.exists(public_dir):
        os.chdir(public_dir)
    else:
        print(f"The intended working dir {public_dir} not found. Exiting.")
        exit()

    server = ThreadingHTTPServer(("127.0.0.1", 8000), MyWebsiteHandler)
    print("Server running on http://127.0.0.1:8000 ...")
    server.serve_forever()
