import socket
import os
import threading

def handle_message(client_socket,client_address):
    # 接收客户端的HTTP请求
    request_data = client_socket.recv(1024).decode()
    # 解析HTTP请求
    request_lines = request_data.split('\r\n')
    request_method, request_path, _ = request_lines[0].split()
    # 构造文件路径
    file_path = os.path.join('D:/py_project/', request_path[1:])
    print(f'文件路径:{file_path}')
    # 检查文件是否存在
    if os.path.exists(file_path) and os.path.isfile(file_path):
        # 读取文件内容
        with open(file_path, 'rb') as file:
            response_data = file.read()
        # 构造HTTP响应报文
        response_header = 'HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n'.format(len(response_data))
        response = response_header.encode() + response_data
    else:
        # 文件不存在，构造404 Not Found响应
        response = 'HTTP/1.1 404 Not Found\r\n\r\nFile Not Found'.encode()
    # 发送HTTP响应到客户端
    client_socket.send(response)
    # 关闭客户端套接字
    client_socket.close()

# 服务器的地址和端口号
server_address = ('10.88.87.125', 3000)  # 请替换为实际的服务器地址和端口号
# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定服务器地址和端口号
server_socket.bind(server_address)
# 监听客户端连接
server_socket.listen(4)
print('等待客户端连接...')
while True:
    # 等待客户端连接请求
    client_socket, client_address = server_socket.accept()
    print(f'接受来自 {client_address} 的连接请求')
    #创建多线程
    client_thread=threading.Thread(target=handle_message,args=(client_socket,client_address))
    client_thread.start()


