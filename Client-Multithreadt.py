import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def send_request(id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        pesan = f"Halo dari client {id}"
        s.sendall(pesan.encode())
        data = s.recv(1024)
        print(f"[BALASAN {id}] {data.decode()}")

def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=send_request, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
