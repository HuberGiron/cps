import socket

HOST = "0.0.0.0"
PORT = 9002

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT))
srv.listen(1)

print(f"[tcp_echo_server] listening on {HOST}:{PORT}")

while True:
    conn, addr = srv.accept()
    print(f"[tcp_echo_server] client {addr}")
    with conn:
        while True:
            data = conn.recv(65535)
            if not data:
                break
            conn.sendall(data)
