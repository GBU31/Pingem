import  os

class IsConnected:
    def __init__(self, ip:str, **kwargs) -> bool:
        self.ip = ip

    def isconnected(self):
        while True:
            ping = os.popen(f'ping {self.ip} -c 1').read()
            print(ping)
            if f'64 bytes from {self.ip}' in ping:
                return True


if __name__ == '__main__':
    print(IsConnected(ip='192.168.1.73').isconnected())