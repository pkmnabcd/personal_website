import os
from sys import exit
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


if __name__ == "__main__":
    # Make the working directory the 'website' dir
    web_dir = os.path.dirname(__file__)
    public_dir = os.path.join(web_dir, "website")
    if os.path.exists(public_dir):
        os.chdir(public_dir)
    else:
        print(f"The intended working dir {public_dir} not found. Exiting.")
        exit()

    # See the following documentation for SimpleHTTPRequestHandler behavior.
    # https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET
    server = ThreadingHTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)
    print("Server running on http://127.0.0.1:8000 ...")
    server.serve_forever()
