import socket

def get_local_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

if __name__ == "__main__":
    print("IP Wi‑Fi đang sử dụng là:", get_local_ip())
