#Finds trail info in text document and orginizes it into a list with dictionaries of the information for each trail
def main():
        print("Would you like to search by length, by location or by difficulty?")
        a=input("L for Length,  O for location, D for difficulty:  ")
        if a=="L":
                find_length()
        elif a="O":
                f=input("Choose one: Northern Maryland, Central Maryland, Baltimore, Southern Maryland, Western Maryland, Eastern Shore:  ")
                find_prop("Where",f)
        else:
                p=input("Choose one: Easy, Moderate, Difficult:  ")
                find_prop("Difficulty",p)
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
    #------------------------------------------------#
	#Find trails that meet certain properties
def find_prop(attr, prop):
    trails = read_trails('trails.txt')
    filtered = []
    for i in trails:
        if i[attr] == prop:
            filtered.append(i["Name"])
    return filtered
def find_length():
    trails = read_trails("trails.txt")
    mirange=input("Input a mile range: <5, 5-10, 10-15, 15-20, 20+ =>")
    validrange=["<5","5-10","10-15","15-20","20+"]
    global filtered=[]
    while mirange not in validrange:
        mirange=input("Input a mile range: <5, 5-10, 10-15, 15-20, 20+ =>")
    for q in trails:
        length=float(q["Length"])
        if mirange=="<5":
            if length<5:
                filtered.append(q["Name"])
        elif mirange=="5-10":
            if length>=5:
                if length<=10:
                    filtered.append(q["Name"])
        elif mirange=="10-15":
            if length>=10:
                if length<=15:
                    filtered.append(q["Name"])
        elif mirange=="15-20":
            if length>=15:
                if length<=20:
                    filtered.append(q["Name"])

        else:
            if length>20:
                filtered.append(q["Name"])
    return(filtered)
#-------------------------------#
#Adds results in webpage
def add_results(result_list):
	file = open("MYPTrails-webpage\index.html", "w")
	trails = read_trails("trails.txt")
	file.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" type="text/css" />
        <link rel='shortcut icon' href='images/favicon.ico' type='image/x-icon'/ > 
        <link href='http://fonts.googleapis.com/css?family=Lato:400,700' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">
        <title>Trail Info</title>
    </head>
    <!-------------------------Begin Body------------------------>
    <body>
        <header>
            <br>
            <br>
        <a href="#"><div class="content-header-wide">
            <h1>Trail Information</h1>
            </div></a>
            </header>
        <br>
        <br>
        <br>''')
	for i in result_list:
		for j in trails:
			if j["Name"] == i:
				dicty = j
				print(dicty)
		file.write('''<div class="content">
        <table>
            <tr>''')
		file.write('''<td><b>Trail Name</b></td>
''')
		name = dicty['Name']
		name_of_trail = '<td>'+name+'</td>'
		file.write(name_of_trail)
		file.write('''</tr>
            <tr>
            <td><b>Trail Length in miles</b></td>
            ''')
		length = '<td>'+dicty['Length']+'</td>'
		file.write(length)
		file.write('''
            </tr>
            <tr>
            ''')
		file.write('''<td><b>Trail Difficulty</b></td>''')
		difficulty = '<td>'+dicty['Difficulty']+'<td>'
		file.write(difficulty)
		file.write('''
	    </tr>
            <tr>
            <td><b>About the Trail</b></td>
            ''')
		file.write('<td>'+dicty['Notes']+'</td>')
		file.write('''</tr>
            </table>
        </div>''')
	file.write('''
   </body>
</html>''')
	file.close()
