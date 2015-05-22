from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urlparse
# import TripletExtector

class TestHTTPHandle(BaseHTTPRequestHandler):

	def __init__(self, *args):
		BaseHTTPRequestHandler.__init__(self, *args)
		# super(TestHTTPHandle, self).__init__(self,*args)
		# self.tripletExtector = TripletExtector()

	def do_GET(self):
		r_sentence= ''
		queryString = urlparse.urlparse(self.path).query
		params = urlparse.parse_qs(queryString)
		r_sentence = self.extractSentence(params)

		self.protocal_version = 'HTTP/1.1'
		self.send_response(200)
		self.send_header("welcome","Contect")
		self.end_headers()
		self.wfile.write("The sentence is: " + r_sentence)

	def extractSentence(self,params):
		r_sentence = params["sentence"][0] if 'sentence' in params else ''
		return r_sentence

def start_server(port):
	print 'start server'
	http_server = HTTPServer(('127.0.0.1',8888), TestHTTPHandle)
	http_server.serve_forever()

def main():
	start_server(0)

if __name__ == '__main__':
	main()