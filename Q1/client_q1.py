import socket

def client():
    HOST = '127.0.0.1'  # Localhost
    PORT = 65432  # Port to connect to

    while True:
        print("\nMenu:")
        print("1. Change Case of String")
        print("2. Evaluate Expression")
        print("3. Reverse String")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '4':
            break

        data = input("Enter input: ")
        message = f"{choice}:{data}"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(message.encode())
            response = s.recv(1024).decode()
            print(f"Server Response: {response}")

if __name__ == "__main__":
    client()