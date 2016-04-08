#Finds trail info in text document and orginizes it
def read_trails(path):
	file = open(path)
	text = file.read()
	trails = []
	g = text.find('>')
	while g != -1:
		dictionary = {}
		name = text[g+1:text.find('\n',g)]
		dictionary['Name'] = name
		g = text.find('Where:',g+1)
		where = text[g+7: text.find('\n', g+1)]
		dictionary['Where'] = where
		g = text.find('Length:',g+1)
		length = text[g+8: text.find('\n', g+1)]
		dictionary['Length'] = length
		g = text.find('Difficulty:',g+1)
		difficulty = text[g+12: text.find('\n', g+1)]
		dictionary['Difficulty'] = difficulty
		g = text.find('Notes:',g+1)
		notes = text[g+6:text.find('>',g+1)]
		dictionary['Notes'] = notes
		trails.append(dictionary)
		g = text.find('>',g+1)
	print(trails)
