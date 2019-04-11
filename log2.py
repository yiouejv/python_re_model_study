import re


def get_file_content(filename):
    with open(filename, 'r') as f:
        return f.read()


def get_ports(content):
    pattern = r'\n([^ ]+.*?) is '
    ports = re.findall(pattern, content)
    ports = list(map(lambda x: x[1:], ports))
    return ports


def get_address(content, ports):
    port = input('输入要查询的端口号>>')
    if port in ports:
        pattern = port + r'.*?Internet address is (.*?)\n  MTU'
        addr = re.search(pattern, content, re.S).group(1)
        return addr
    else:
        print('端口号有误，请重新输入！')
        get_address(content, ports)


def main():
    content = get_file_content('book.txt')
    ports = get_ports(content)
    addr = get_address(content, ports)
    print(addr)


if __name__ == '__main__':
    main()
