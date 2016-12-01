import re
open_tag_re = re.compile('<[a-zA-Z_]+|</[a-zA-Z_]+')

def element_seperation(xml):
	global elements
	elements = open_tag_re.findall(xml)
	for x in range(len(elements)):
		elements[x] = elements[x].replace('<','')
		elements[x] = elements[x].replace('/','')

def declaration_error(xml):
	if(not xml.count('<?') == 1):
		return 'declaration not opened'
	elif(not xml.count('?>') == 1):
		return 'declaration not closed'
	
def xml_body_error(xml):
	if(xml.count('<') < xml.count('>')):
		return 'xml tag open error'
	elif(xml.count('<') > xml.count('>')):
		return 'xml tag close error'
	elif(not xml.count('\'') % 2 == 0):
		return 'unclosed \''

def xml_parsing():
	x = 1
	seperator = []
	seperator.append(elements[0])
	while len(seperator) > 0 and x < len(elements):
		seperator.append(elements[x])
		print(seperator,x)
		size = len(seperator)
		if seperator[size-1] == seperator[size-2]:
			temp = seperator[len(seperator)-1]
			seperator.remove(temp)
			seperator.remove(temp)
		x += 1

def get_input():
	filename = input('Enter filename: ')
	with open(filename, 'r',buffering =-1) as file:
            xml = file.read()
	element_seperation(xml)
	print(len(elements))
	print(declaration_error(xml))
	print(xml_body_error(xml))
	xml_parsing()

get_input()