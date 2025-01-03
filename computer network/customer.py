from socket import *
import time
list_rtt=[]
# 服务器的地址和端口号
server_address = ('10.88.87.125', 2000)
# 创建客户端套接字，使用IPv4地址和UDP协议
clientSocket = socket(AF_INET, SOCK_DGRAM)
#设置超时
clientSocket.settimeout(1.0)
# 发送10个ping消息
for i in range(1, 11):
    # 构造ping消息
    message = f'Ping {i}'
    # 记录发送时间
    send_time = time.time()
    # 发送ping消息到服务器
    clientSocket.sendto(message.encode(), server_address)
    try:
        # 接收服务器的响应
        response, _ = clientSocket.recvfrom(1024)
        # 计算往返时间RTT
        rtt = (time.time() - send_time)
        list_rtt.append(rtt)
        # 打印响应消息和RTT
        print(f'收到响应: {response.decode()}，RTT = {rtt:.6f}秒')
    except:
        # 如果超时，打印请求超时
        print(f'请求超时')
#计算最小，最大，平均RTT以及丢包率
list_rtt.sort()
len=list_rtt.__len__()
sum=0.0
for item in list_rtt:
    sum+=item
sum/=len
percent=(10-len)/10
print(f'最小RTT = {list_rtt[0]:.6f}秒,最大RTT = {list_rtt[len-1]:.6f}秒,平均RTT = {sum:.6f}秒,丢包率 = {percent:.0%}')
# 关闭客户端套接字
clientSocket.close()


