import socket
import time

def udp_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    
    message = "time"
    start_time = time.time()  
    client_socket.sendto(message.encode(), (host, port))

   
    data, addr = client_socket.recvfrom(1024)
    end_time = time.time()  

    
    delay = end_time - start_time

    print(f"Текущее время от сервера: {data.decode()}")
    print(f"Задержка: {delay:.6f} секунд")

if __name__ == "__main__":
    udp_client()