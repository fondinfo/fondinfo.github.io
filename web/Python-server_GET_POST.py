from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        # allows a request originating from another website
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()

    def do_GET(self):      
        self._set_headers()
        url = urlparse(self.path)

        self.wfile.write(bytes("<html><head><title>Server Page</title></head>\n", "utf-8"))
        self.wfile.write(bytes("<body>\n", "utf-8"))
        self.wfile.write(bytes("<p>Method GET</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>Local uri: %s</p>\n" % url.path, "utf-8"))
        self.wfile.write(bytes("<p>Query: %s</p>\n" % url.query, "utf-8"))
        self.wfile.write(bytes("</body></html>\n", "utf-8"))

    def do_POST(self):
        self._set_headers()
        data = self.rfile.read(int(self.headers['Content-Length']))
        with open('data_processed.txt', 'ab') as file:
            file.write(data)        
        file.close()
        self.wfile.write(bytes("<html><head><title>Server Page</title></head>\n", "utf-8"))
        self.wfile.write(bytes("<body>\n", "utf-8"))        
        self.wfile.write(bytes("<p>Method POST</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>Data received: %s</p>\n" % data, "utf-8"))
        self.wfile.write(bytes("<p>Data stored in file data_processed.txt</p>\n", "utf-8"))
        self.wfile.write(bytes("</body></html>\n", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
