import re

def toke(text):
	text = text.split()
	words = list()
	for index,key in enumerate(text):
		word_found = re.findall(r"[@#]?[A-Za-z0-9]+|[^A-Za-z0-9\s]",key) #returns list

		if word_found:
			words.extend(word.lower() for word in word_found)
	return words