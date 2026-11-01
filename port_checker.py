from datetime import datetime
import socket


targets = []
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("targets.txt") as f:
    for line in f:
        try:
            line = line.strip()
            host, port = line.split(':')
            port = int(port)
        except ValueError:
            print(f"Строка пропущена: {line!r}")
            continue      
        targets.append((host, port))

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=2):
            status = "Успешное подключение"
            return status
    except TimeoutError:
        status = "Таймаут превышен"
        return status
    except ConnectionRefusedError:
        status = "Порт закрыт"
        return status
    except socket.gaierror:
        status = "Имя хоста не найдено"
        return status


with open ('results.txt', 'a') as file:
    file.write(f"\n{current_datetime}\n")
    for num, (host, port) in enumerate(targets, 1):
        status = check_port(host, port)
        result_line = f"{num}. {host}:{port} - {status}"
        print(result_line)
        file.write(f"{result_line}\n")
