
with open('nginx_logs.txt', 'r') as logs_nginx:
    result = []

    for line in logs_nginx:
        result_list = []

        remote_addr = line[:line.find("- -", 0, len(line))]

        start_request_type = line.rfind('] "', 0, len(line))
        end_request_type = line.rfind(" /", 0, len(line))

        request_type = line[start_request_type + 3:end_request_type]

        start_requested_resource = line.rfind(" /", 0, len(line))
        end_requested_resource = line.rfind(" HTTP", 0, len(line))

        requested_resource = line[start_requested_resource:end_requested_resource].strip()

        result_list.append(remote_addr)
        result_list.append(request_type)
        result_list.append(requested_resource)

        result.append(tuple(result_list))

    print(result)