import socket
import time 
def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем сокет
    start = time.time()
    client_socket.connect(('localhost', 12345))  # Подключаемся к серверу

    
    client_socket.sendall(b"Hello, Server")
    response = client_socket.recv(1024)
    print('Сервер ответил:', response.decode())

    client_socket.close()  # Закрываем соединение
    print(f"Время работы: {time.time() - start} ")
if __name__ == "__main__":
    connect_to_server()