import BaseHTTPServer
import SocketServer
import cgi

PORT = 8080

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_POST(self):
	    ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
   	    if ctype == 'multipart/form-data':
        	postvars = cgi.parse_multipart(self.rfile, pdict)
   	    elif ctype == 'application/x-www-form-urlencoded':
        	length = int(self.headers.getheader('content-length'))
        	postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    	    else:
        	postvars = {}	
	    for k, v in postvars.items(): print "%s: %s"%(k,v)
	    self.send_response(200)
            self.end_headers()
            self.wfile.write("ok")
            return

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
