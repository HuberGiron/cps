import socket

HOST = "0.0.0.0"
PORT = 9001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"[udp_echo_server] listening on {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(65535)
    sock.sendto(data, addr)
