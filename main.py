import webbrowser
import os
#--------------Opens Webpage-----------------#
def openpage():
        webbrowser.open('file://' + os.path.realpath('Trails-webpage\index.html'))
#Asks user how they want to search up trails by
def main():
        print('''
╔==============================================================================╗
║                                    Trails                                    ║
║                                                                              ║
║                  A hiking trail filter for trails in Maryland.               ║
║                                                                              ║
║                           [Fullscreen Recommended.]                          ║
╚==============================================================================╝''')
        print("")
        print("How would you like to browse the list of trails?")
        print("")
        a=input("Type 'L' for Length,  'O' for Location, 'D' for Difficulty, 'A' for All Trails: ").upper()
        print("")
        validfilter=["L","O","D","A","V"]
        while a not in validfilter:      
                a=input("'L' for Length,  'O' for Location, 'D' for Difficulty, 'A' for All Trails: ").upper()
                print("")
        if a.upper()=="L":
                find_length()
        elif a.upper()=="O":
                f=input("Choose one: 'Northern Maryland', 'Central Maryland', 'Baltimore', 'Southern Maryland', 'Western Maryland', or 'Eastern Shore':  ")
                if (' ' in f):
                        space = f.split()
                        f = ''
                        for i in space:
                                f = f + i[0].upper() + i[1:].lower() + ' '
                        f = f[:-1]
                else:
                        f = f[0].upper() + f[1:].lower()
                find_prop("Where",f)
        elif a.upper()=="A":
                find_all()
        elif a.upper()=="V":
                f=[]
                add_results(f)
        else:
                p=input("Choose one: 'Easy', 'Moderate', 'Difficult':  ")
                p = p[0].upper() + p[1:].lower()
                find_prop("Difficulty",p)
        openpage()
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
    #------------------------------------------------#
#Adds results in webpage
def add_results(result_list):
        file = open("Trails-webpage\index.html", "w")
        trails = read_trails("trails.txt")
        file.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" type="text/css" />
        <link rel='shortcut icon' href='images/favicon.ico' type='image/x-icon'/ > 
        <link href='http://fonts.googleapis.com/css?family=Lato:400,700' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
        <title>Trail Info</title>
    </head>
    <!-------------------------Begin Body------------------------>
    <body>
    
        <header>

            <div class="right"><a class="btn" href="#"><i class="fa fa-home fa-2x" aria-hidden="true"></i></a></div><br><br>
        <a href="#"><div class="content-header-wide">
            <h1>Trails</h1>
            </div></a>
            </header>
        <br>
        <br>
        <br>''')
        if result_list==[]:
                file.write('''<br><br><br><center><div id="noshow"><a href="#"><b>There are no trails that match the selected filter.</b></a></div></center>''')
        for i in result_list:
                for j in trails:
                        if j["Name"] == i:
                                dicty = j
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
                file.write('<td>'+dicty['Notes']+'</td></tr>')
                file.write('''<tr>
<td><b>External Links</b></td>''')
                sources = ''
                file.write('<td>')
                file.write('''<div id="navcontainer"><ul>''')
                for e in dicty['Sources']:
                        href = '<li>'+'<a href=' + e + ' target="_blank">' + e + '</a>'+'</li><br>'
                        if e != "":
                                file.write(href)
                file.write('</ul></div></td>')
                file.write('''</tr>''')
                file.write(''' </table>
        </div><br><br>''')
        file.write('''
   </body>
   <footer>
           <br><br><br><span id="Bottom"><div class="content-small">Happy Hiking!<br>Matt Gu & Tejas Guha | 2016<hr>	   
           <div id="footer"><a href="https://github.com/mattgu16/Trails">Github Repository</a>
           <a href="https://travis-ci.org/mattgu16/Trails">Travis Build Log</a>
           <a href="stats.html">Cool Stats</a>
   </footer>        
</html>''')
        file.close()
        #---------------------------------------#
        #Find trails that meet certain properties
#Find trails that meet at certain difficulty or location
def find_prop(attr, prop):
    trails = read_trails('trails.txt')
    global filtered
    filtered = []
    for i in trails:
        if i[attr] == prop:
            filtered.append(i["Name"])
    add_results(filtered)
#Finds all trails
def find_all():
    trails = read_trails('trails.txt')
    global filtered
    filtered = []
    for i in trails:
            filtered.append(i["Name"])
    add_results(filtered)
#Finds trails that meet a length
def find_length():
    trails = read_trails("trails.txt")
    mirange=input("Input a mile range: '<5', '5-10', '10-15', '15-20', 20+ => ")
    validrange=["<5","5-10","10-15","15-20","20+"]
    global filtered
    filtered=[]
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
        add_results(filtered)       
#---------------Running Program----------------#
while 1>0:
        main()
