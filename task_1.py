"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""
import platform
from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(ip_addresses, timeout=100, req=1, info=True):
    param= '-n' if platform.system().lower() == 'windows' else '-c'
    result = []
    for address in ip_addresses:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        ping = Popen(f"ping {address} -w {timeout} {param} {req}", shell=False, stdout=PIPE)
        ping.wait()
        if ping.returncode == 0:
            if info:
                print(f"Узал '{address}' доступен")
            result.append((address, True))
        else:
            if info:
                print(f"Узел '{address}' недоступен")
            result.append((address, False))
    return result


if __name__ == '__main__':
    list_ip_addresses = ['google.com', 'localhost', '192.168.0.1', '45.9.216.188', '0.0.0.0']
    host_ping(list_ip_addresses)
