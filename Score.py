import re

def score(text, cens_word):
    text_list = re.findall(r'\b[A-Za-z0-9]+\b', text.lower())  
    if not text_list:  
        return 0.0

    count_vulgar = sum(1 for word in text_list if word in cens_word)
    total_words = len(text_list) 

    value_score = count_vulgar / total_words
    return value_score

with open("Slang_data/en.txt", 'r') as cens_lang:
    cens_word = {line.strip().lower() for line in cens_lang}
