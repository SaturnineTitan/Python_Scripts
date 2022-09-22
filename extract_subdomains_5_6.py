
with open("/usr/share/wordlists/wfuzz/general/subdomains-10000.txt", "r+") as file:
	subdomains_5_6 = []
	while True:
		line = file.readline().strip()

		if not line:
			break
		if len(line) == 5 or len(line) == 6:
			subdomains_5_6.append(line)
file.close()

with open("subdomains_5_6.txt", "a") as file:
	for domain in subdomains_5_6:
		file.write(domain)
		file.write("\n")
file.close()
