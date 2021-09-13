import socket
import http.client


hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
external_ip = conn.getresponse().read()


def getNetworkIp():
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('', 0))
    return s.getsockname()[0]


if __name__ == "__main__":
    print(hostname, IP, external_ip)
    print ("HostName: ",getNetworkIp())