"""
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""
import ipaddress
from task_1 import host_ping


def host_range_ping(ip_adress, num):
    """
    Функция перебирает диапазон ip-адесов. только последниий актет
    Полученный арес проверяет на доступность
    :param ip_adress:
    :param num:
    :return:
    """
    list_ip_address = []
    [list_ip_address.append(ipaddress.ip_address(ip + i)) for i in range(num)]
    host_ping(list_ip_address)

# IP1 = input("Введите 1-ый адрес:")
# IP2 = input("Введите 2-ый адрес:")

ip = ipaddress.ip_address('45.9.216.188')
num = 5
host_range_ping(ip, num)

