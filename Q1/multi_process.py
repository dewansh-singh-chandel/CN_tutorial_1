import socket
import multiprocessing


def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        data = conn.recv(1024).decode()
        if not data:
            return
        choice, value = data.split(":", 1)
        
        if choice == '1':
            result = value.swapcase()
        elif choice == '2':
            try:
                result = str(eval(value))
            except Exception as e:
                result = f"Error: {str(e)}"
        elif choice == '3':
            result = value[::-1]
        else:
            result = "Invalid Choice"

        conn.sendall(result.encode())


def multi_process_server():
    HOST = '127.0.0.1'
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        s.bind((HOST, PORT))
        s.listen()
        print("Multi-Process Server Running...")
        while True:
            conn, addr = s.accept()
            process = multiprocessing.Process(target=handle_client, args=(conn, addr))
            process.start()
            conn.close()

if __name__ == "__main__":
    multi_process_server()