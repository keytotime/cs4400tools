#!/usr/bin/python
import requests
import threading
import socket

test_site = "http://danielkenner.com/"


#lab1-28.eng.utah.edu 2118
#lab1-13.eng.utah.edu 2112
#lab1-12.eng.utah.edu 2115
proxy_server = "lab1-13.eng.utah.edu"
proxy_port = 2112

number_of_tests = 100

def main():
  for i in range(number_of_tests):
    t = threading.Thread(target=worker)
    t.start()

def worker():
  #print "worker"
  s = mysocket()
  s.connect(proxy_server, proxy_port)
  message = "GET "+test_site+" HTTP/1.0\r\n\r\n"
  s.mysend(message)
  ret = s.myreceive()
  print "Worker Finished"
  return
  

#got from the python documentation
class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while True:
            chunk = self.sock.recv(2048)
            if chunk == '':
              break
                #raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)

if __name__ == '__main__':
  main()