import socket
import time


# Создаем функцию сканера. В параметрах принимаем адрес хоста и список с портами
def scan_ports(host, ports):
    print("." * 20)
    time.sleep(1)
    print("Ожидай, идет сканирование портов!\n")
    # Считаем колличество открытых портов
    p = 0
    # В цикле перебираем порты из списка
    for port in ports:
        # Создаем сокет
        s = socket.socket()
        # Ставим тайм-аут в одну cекунду
        s.settimeout(1)
        # Ловим ошибки
        try:
            # Пробуем соединиться, хост и порт передаем как список
            s.connect((host, port))
        # Если соединение вызвало ошибку
        except socket.error:
            # тогда ничего не делаем
            pass
        else:
            print(f"{host}: {port} порт активен")
            # Закрываем соединение
            s.close()
            p += 1
    print(f"\nАктивных портов найдено: {p} \nСканирование завершено!")


# Создаем функцию ручного ввода порта
def user_vybor():
    try:
        in_user = int(input("Введите номер нужного порта... Для возврата введите '0'\n"))
        if in_user == 0:
            return
        ports_user = [in_user]
        scan_ports(host, ports_user)
    except:
        print("Порт введен неверно!")
        time.sleep(1)
        user_vybor()


# Создаем функцию ввода диапозона портов
def user_vybor_range():
    try:
        in_user = int(input("Введи номер начального порта диапозона... Для возврата введите '0'\n"))
        if in_user == 0:
            return
        in_user2 = int(input("Введите номер конечного порта диапозона... Для возврата введите '0'\n"))
        if in_user == 0:
            return
        ports_range = range(in_user, in_user2)
        scan_ports(host, ports_range)
    except:
        print("Порт введен неверно!")
        time.sleep(1)
        user_vybor_range()


# Список портов для сканирования
ports_pop = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514,
             515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000,
             20000]

# Основной цикл программы
print("\nПриветствую тебя в сканере портов!")
time.sleep(1)
while True:
    time.sleep(1)
    host = input('\nДля выхода нажми "0"\nВведи имя сайта без http/https или IP-адрес: \n')
    if host == "0":
        print("\nВыход из программы...")
        break
    time.sleep(1)
    print(f"\nКакие порты {host} будем сканировать? \n\n1 - Стандартные порты \n2 - Диапозон портов \n3 - Один порт \n0 - Выход из программы")
    vybor = input()
    if vybor == "1":
        scan_ports(host, ports_pop)
    elif vybor == "2":
        user_vybor_range()
    elif vybor == "3":
        user_vybor()
    elif vybor == "0":
        print("\nВыход из программы...")
        break
    else:
        print("\nНеверный ввод...")
