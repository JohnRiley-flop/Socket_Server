import socket
import socket_client
import getpass

#Compliment method to "Connect a client".
def connect_to_server(socket_address, socket_port, socket_password):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((socket_address, socket))
    print(f"Connected to server at {socket_address}:{socket_port}")
    client_socket.send(socket_password.encode('utf-8'))
    # Receive the server's response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server says: {response}")
    
    # Close the connection
    client_socket.close()
    
    print("An error has occurred.")
    return False


def main():
    print("Welcome to the socket client program. Please provide the necessary information so we can get you connected.")
    addr = input("Please enter the address of the socket (local_machine/127.0.0.1): ")
    port = input("Please enter the port of the socket (local/54321): ")
    passwd = getpass.getpass(prompt="Please enter the socket's password (won't echo): ")
    connect_to_server(addr, port, passwd)



if __name__ == '__main__':
    main() 