import socket
import sys
# from pwmTest import pwmTest
from thread import *
host = ''
port = 4000
print("port" , port)

class Slin_socket_Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connect = False
        # try:
        #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # except socket.error,msg:
        #     print "Unable to create socket"
        #     sys.exit()
        print "Socket created."
        # self.pwm = pwmTest()

    def bind(self):
        try:
            self.sock.bind((host,port))
        except socket.error,msg:
            print "Bind failed. Closing..."
            sys.exit()
        print "Socket bound."
    def run(self):
        self.sock.listen(1)
        while 1:
            print "Socket Listening"
            conn, addr = self.sock.accept()

            if (self.connect) :
                conn.close()
                print("close other sokcet")
                continue
            self.connect = not self.connect
            print "Connected to %s:%s"%(addr[0],addr[1])
            start_new_thread(threadWork, (conn, self))
def threadWork(client , slin_socket_instans):
    while True:
        income = client.recv(1024)
        if income == "" :
            print("connect break")
            break
        # if income != "":
        #     pass
            # print(income[:])

        if income[:4] == "slin" :

            print("slin:" + income[4:6])
            motor1status = income[4]
            motor2status = income[5]
            # slin_socket_instans.pwm.go(int(motor1status),int(motor2status))
            # slin_socket_instans.pwm.forwake()
        if income[:4] == "exit" :
            print("exit socket close")
            break
    client.close()
    slin_socket_instans.connect = not slin_socket_instans.connect



def main():

    serv = Slin_socket_Server()
    serv.bind()
    serv.run()

if __name__ == "__main__":
    main()
