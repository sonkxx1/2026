from ipaddress import *

net = ip_network('205.99.68.249/21', False)

print(list(net.hosts())[-1])