with open('output.txt','rb') as file:
	text = file.read()

with open('answer.txt', 'wb') as file:
	file.write(text[::-1])