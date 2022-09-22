
lowercase = 'abcdefghijklmnopqrstuvwxyz'


with open('two_letters.txt', 'a') as file:
	for x in range(len(lowercase)):
		string = lowercase[x]
		for y in range(len(lowercase)):
			string += lowercase[y]
			file.write(string + '\n')
			string = lowercase[x]
file.close()
