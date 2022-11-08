import re

filename = input("enter filename")
with open(filename) as f:
	
		line = f.read()
		#print(line)
		ipaddrs = re.findall(r"\"PublicIp\"\"\:\x20\"\"((?:\d{1,3}\.){3}\d{1,3})\"",line)
		#print(ipaddrs)
		with open("iplist.csv","w") as output:
			output.write("address\n")
			ipaddrs = set(ipaddrs)
			for i in ipaddrs:
				output.write(f"{i}\n")
