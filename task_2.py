"""
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""
from ipaddress import ip_network, ip_address
from task_1 import host_ping


def host_range_ping(_subnet_address, start_address=None, end_address=None, info=True):
    """
    Функция перебирает диапазон ip-адесов. только последниий актет
    Полученный арес проверяет на доступность
    :param info:
    :param _subnet_address:
    :param start_address:
    :param end_address:
    """
    start_index = -1
    end_index = 254

    try:
        subnet = ip_network(_subnet_address)
        ip_addresses = [subnet.network_address + i for i in range(1, subnet.num_addresses)]
        if start_address is not None:
            start_address = ip_address(start_address)
            if start_address in ip_addresses:
                start_index = ip_addresses.index(start_address) - 1
        if end_address is not None:
            end_address = ip_address(end_address)
            if end_address in ip_addresses:
                end_index = ip_addresses.index(end_address)+1
    except Exception:
        print(f"Ошибка!")
    else:
        if start_address is not None and end_address is None:
            ip_addresses = [address for address in ip_addresses if ip_addresses.index(address) > start_index]
        elif end_address is not None and start_address is None:
            ip_addresses = [address for address in ip_addresses if ip_addresses.index(address) < end_index]
        elif start_address is not None and end_address is not None:
            ip_addresses = [address for address in ip_addresses if
                            start_index < ip_addresses.index(address) < end_index]
        return host_ping(ip_addresses, info=info)


if __name__ == "__main__":
    subnet_address = '45.9.216.0/24'
    start_address = '45.9.216.1'
    end_address = '45.9.216.18'
    host_range_ping(subnet_address, start_address=start_address, end_address=end_address)

