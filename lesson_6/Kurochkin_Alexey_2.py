
with open('nginx_logs.txt', 'r') as logs_nginx:
    dict_ip = {}

    for line in logs_nginx:
        remote_addr = line[:line.find("- -", 0, len(line))].strip()

        if dict_ip.get(remote_addr, None) is None:
            dict_ip.setdefault(remote_addr, 1)
        else:
            values = dict_ip.get(remote_addr)
            old_key = remote_addr

            del dict_ip[old_key]
            dict_ip.setdefault(remote_addr, values + 1)

    result = max(dict_ip.values(), key=lambda i: int(i))

    for key, values in dict_ip.items():
        if values == result:
            print(f'Spamer {key}, request {values}')



