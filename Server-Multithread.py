import socket
import threading

HOST = '127.0.0.1'  # localhost
PORT = 5000

def handle_client(conn, addr):
    print(f"[TERHUBUNG] Client {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"[DARI {addr}] {data.decode()}")
        conn.sendall(f"Server menerima: {data.decode()}".encode())
    conn.close()
    print(f"[PUTUS] Client {addr}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[MENUNGGU KONEKSI] Server berjalan di {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[JUMLAH KONEKSI AKTIF] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
