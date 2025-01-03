import socket
# 服务器的地址和端口号
server_address = ('10.88.87.125', 3000)
filename = '/home.html'
# 创建客户端套接字，使用IPv4地址和TCP协议
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接到服务器
client_socket.connect(server_address)
# 构造HTTP GET请求
http_request = f'GET {filename} HTTP/1.1\r\nHost: {server_address[0]}\r\n\r\n'
# 发送HTTP请求到服务器
client_socket.send(http_request.encode())
# 接收服务器的响应
response = b''
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data
# 打印响应内容
print(response.decode())
# 关闭客户端套接字
client_socket.close()
