import socket
import threading
import os
import argparse
import time

HOST = '127.0.0.1'
PORT = 65432


def handle_request(request):
    """Processes the client request based on the selected option."""
    try:
        choice, data = request.split(",", 1)
        if choice == '1':
            return data.swapcase()  # Swap uppercase and lowercase
        elif choice == '2':
            return str(eval(data))  # Evaluate mathematical expression
        elif choice == '3':
            return data[::-1]  # Reverse the string
        else:
            return "Invalid Choice"
    except Exception as e:
        return str(e)

def process_client(conn, addr):
    """Handles a client request."""
    print(f"Connected by {addr}")
    request = conn.recv(1024).decode()
    response = handle_request(request)
    time.sleep(3)
    conn.sendall(response.encode())
    conn.close()
    print(f"Connection closed {addr}")

def multi_process_server():
    """Multi-Process Server: Creates a new process for each client."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(102)
        print("Running Multi-Process Server...")

        while True:
            conn, addr = server_socket.accept()
            pid = os.fork()
            if pid == 0:  # Child process
                process_client(conn, addr)
                os._exit(0)  # Exit child process
            else:
                conn.close()  # Parent closes its connection


if __name__ == "__main__":
    multi_process_server()