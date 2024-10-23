with open ('../data/Harry-Potter-Text.csv', 'r') as file:
    content = file.read()

content

#Split 'content' by new lines:
lines = content.split('\n')

#Split 'content' by spaces:
words = content.split(' ')

#Find out how many lines there are in variable 'lines':
print(len(lines))

#Return the twelth word in 'words':
words[12]

#Return the first three lines in 'lines':
lines[:3]

#Return the last 7 words in 'words':
words[-7:]

#splits 'lines' by full stops and stores this in 'fields':
fields = lines[0].split('. ')
print (fields)

'''calling pprint module allows the dictionary to be printed on several lines rather than just 1

        There are 4 entries within fields and the dictionary stores each entry to a line number

        The dictionary is then printed using pprint (Pretty Print)

'''

from pprint import pprint

dictionary = {
    'line 1': fields[0],
    'line 2': fields[1],
    'line 3': fields[2],
    'line 4': fields[3],
}

pprint(dictionary)