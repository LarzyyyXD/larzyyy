import socket
import datetime
def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет
    server_socket.bind(('localhost', 12345))  # Привязываем сервер к порту

    print("UDP сервер запущен и ожидает данные...")
    data, addr = server_socket.recvfrom(1024)  # Получаем данные
    if data.decode() == 'time':
        print(f"Запрос клиента: {data.decode()}")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        server_socket.sendto(current_time.encode(), addr)
    server_socket.close()

if __name__ == "__main__":
    udp_server()