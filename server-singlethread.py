import socket

HOST = '127.0.0.1'
PORT = 6000

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)  # hanya 1 client pada satu waktu
    print(f"[MENUNGGU CLIENT] Server berjalan di {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"[TERHUBUNG] {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[DARI {addr}] {data.decode()}")
            conn.sendall(f"Server menerima: {data.decode()}".encode())
        conn.close()
        print(f"[PUTUS] Client {addr}")

if __name__ == "__main__":
    main()
