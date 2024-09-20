import socket
import socketserver
import socket_server

#---server class-------------------------------------------------------------------------------------------------
class SocketServer:
    #initialize class and default tarter variables
    __isRunning = False
    __clientList = []
    __serverIp = '0.0.0.0'
    __serverPort = 12345
    __serverPassword = "password"

    #socket server
    __socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #constructor
    def __init__(self, hostIp: str, hostPort: int, hostPassword: str):
        self.__serverIp = hostIp
        self.__serverPort = hostPort
        self.__serverPassword = hostPassword

    #Start server connection and bind to address + port.    
    def startServer(self):
        self.__socketObj.bind((self.__serverIp, self.__serverPort))
        print(f"Server can listen on {self.__serverIp}:{self.__serverPort}")
        #password protect these next few lines
        
    def closeServer(self):
        self.__isRunning = False
    #initia
    
    def connectClient(self):
        self.__socketObj.listen(5)
        conn, addr = self.__socketObj.accept()
        with conn:
            print(f"Connected by {addr}")
            self.receiveFile('received_file.txt', conn)
            print("File received and saved as 'received_file.txt'")

    #Get the online status of the server
    def getStatus(self) -> str:
        return f"IP: {self.__serverIp}\nPORT: {self.__serverPort}\nRunning: {self.__isRunning}"
    
    #
    def receiveFile(self, filename, connection):
        with open(filename, 'wb') as f:
            while True:
                data = connection.recv(1024)  # Receive data in chunks
                if not data:
                    break
                f.write(data)




def listCommands():
    commands = ["(start) start server", "(stop) stop server", "(status) server status","(connect) connect a client", "(clients) list all clients"]
    #max_length = max(len(command) for command in commands)
    #total_width = max_length + 20
    #for command in commands:
    #    print(f'[{command.center(max_length):^}]'.center(total_width))
    print("Server commands. Please type the term in parenthesis to execute.")
    for command in commands:
        print(f">> {command}")



#---server actions-----------------------------------------------------------------------------------------------


if __name__ == '__main__':
    newIp = input("Enter the IP the server will use (local/127.0.0.1): ")
    newPort = int(input("Enter the port that the server will listen on (local/54321 or something): "))
    password = input("Enter a password to protect the server: ")
    server = SocketServer(newIp, newPort, password)
    nextAction = ''
    print("\nTo get started, type \"list\" to see a list of server commands. To stop the program, enter \"quit\".")
    print("Welcome to the socket server program.")
    while nextAction != 'quit':
        nextAction = input("Enter command: ")
        match (nextAction):
            case 'list':
                listCommands()
            case 'status':
                print(server.getStatus())
            case 'start':
                server.startServer()
            case 'close':
                server.closeServer()
            case 'connect':
                server.connectClient()
            case _ :
                print("Input unrecognized.")
                continue
    del(server)
    print("Quitting program. Ciao!")