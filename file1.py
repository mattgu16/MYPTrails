#Finds trail info in text document and orginizes it into a list with dictionaries of the information for each trail
def read_trails(path):
	file = open(path, encoding="utf8")
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
		notes = text[g+6:text.find('Source:',g+1)]
		dictionary['Notes'] = notes
		g = text.find('Source:', g+1)
		comma = text.find(',', g+1)
		newline = text.find('\n',g)
		source = ''
		if newline >= comma:
			source = [text[g+8: comma], text[comma+2: newline]]
		if newline <= comma:
			source = [text[g+8: text.find('\n', g+1)]]
		dictionary['Sources'] = source
		trails.append(dictionary)
		g = text.find('>',g+1)
	return trails
