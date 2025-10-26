import socket
import time

HOST = '127.0.0.1'
PORT = 6000

def main():
    for i in range(10):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            pesan = f"Request ke-{i}"
            s.sendall(pesan.encode())
            data = s.recv(1024)
            print(f"[BALASAN {i}] {data.decode()}")
            time.sleep(0.5)  # jeda agar terlihat bergiliran

if __name__ == "__main__":
    main()
