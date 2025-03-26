import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем сокет
    server_socket.bind(('localhost', 12345))  # Привязываем сокет к хосту и порту
    server_socket.listen(5)  # Начинаем прослушивание

    print("Сервер ожидает подключений...")
    client_socket, client_address = server_socket.accept()  # Принимаем подключение

    print(f"Подключен клиент: {client_address}")
    
    response = client_socket.recv(1024)
    client_socket.sendall(response)  
    print("Клиент отправил:", response.decode())  # Выводим сообщение
    client_socket.close()  # Закрываем соединение

if __name__ == "__main__":
    start_server()