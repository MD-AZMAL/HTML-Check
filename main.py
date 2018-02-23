
file = open('test.html','r')

reader = file.read()

elements = reader.split('<')

cl_tag = []
op_tag = []


for el in elements:
	if '>' in el:
		if '/' in el:
			cl_tag.append(el.split('>')[0].replace('/',''))
		else:
			op_tag.append(el.split('>')[0])

for el in op_tag:
	if ('!DOCTYPE' or 'a href' or 'br' or 'link' or 'meta') in el: # remove some basic singular tags
		op_tag.remove(el) 

print(op_tag)
print('\n\n\n')
print(cl_tag)
