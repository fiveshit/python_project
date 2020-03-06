import socket
import struct
import sys
class TFTP_upload:
    def __init__(self):
        #self.file_name = sys.argv[1]
        self.ip_addr = sys.argv[1]
        self.port_num = sys.argv[2]
        self.SocketClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.SocketClient.connect((self.ip_addr,int(self.port_num)))
    def upload(self):
        while True:
            data = input("input:")
            filenameLen = str(len(data))
            cmdBuf = struct.pack(("!H%ssb5sb" %filenameLen).encode("utf-8"),1,data.encode("utf-8"),0,b"octet",0)
        #data = input("input:")
        #data = data.encode('utf-8')
            print(filenameLen)
            print(data)
            self.SocketClient.sendall(cmdBuf)
            if data == "exit":
                break
            rev_data = self.SocketClient.recv(1024)
            print("rev:",repr(rev_data))
        self.SocketClent.close()

if __name__=='__main__':
    start = TFTP_upload()
    start.upload()
    

