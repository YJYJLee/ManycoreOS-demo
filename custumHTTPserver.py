# import http.server
# import socketserver
# import json

# PORT = 8000

# class Handler(http.server.SimpleHTTPRequestHandler):
#     def do_POST(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()

#         # self.wfile.write(json.dumps({"success": True}))

#         content_length = int(self.headers['Content-Length'])
#         json_string = self.rfile.read(content_length)
#         data = json.loads(json_string)
#         print(data)

# httpd = socketserver.TCPServer(("", PORT), Handler)

# print("serving at port", PORT)
# httpd.serve_forever()

import socketserver
import http.server
import logging
import cgi

PORT = 8000

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

        with open("data.txt", "w") as file:
            for key in form.keys(): 
                file.write(str(form.getvalue(str(key))) + "\n")

Handler = ServerHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()