from ipaddress import *

ip_1 = ip_address('200.154.190.12')
ip_2 = ip_address('200.154.184.0')

for mask in range(16,31)[::-1]:
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net.hosts() and ip_2 in net.hosts():
        print(mask)
        break

