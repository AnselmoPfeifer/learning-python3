import nmap

"""
pip3 install python-nmap
"""

scanner = nmap.PortScanner()

print('Welcome, this is a simple nmap automation tool using!')
print('-'*53)

ip_address = input('Please enter the IP address you want to scan: \n')
print('The IP address is: ', ip_address)

response = input("""Please enter the type of scan you want to run 
1) SYNN ACK Scan
2) UDP Scan
3) Comprehensive Scan
""")

if response == str(1):
    print('Nmap version', scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('Open Port: ', scanner[ip_address]['tcp'].keys())

elif response == str(2):
    print('Nmap version', scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('Open Port: ', scanner[ip_address]['udp'].keys())

elif response == str(3):
    print('Nmap version', scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('Open Port: ', scanner[ip_address]['tcp'].keys())
    print(scanner)

elif response >= str(4):
    print('Please print valid option!')