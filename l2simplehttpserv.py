import http.server
import socketserver
import socket

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/sekarang':
            self.path = 'batt_curr_stat.html'
        if self.path == '/log':
            self.path = 'battery_log.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler
IP=socket.gethostbyname(socket.gethostname())
PORT = 8800
my_server = socketserver.TCPServer((IP, PORT), handler_object)

def main2():
    my_server.serve_forever()

if __name__ == '__main__':  
    main2()