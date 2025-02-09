import socket
import sys

HOST = '127.0.0.1'  # Update this if running on localhost or another machine
PORT = 65432

def run_client():
    """Connects to the server, sends a request, and prints the response."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            message = "3:hello"  # "3" indicates the reverse operation
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_client()
