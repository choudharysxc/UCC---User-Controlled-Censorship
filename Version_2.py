import joblib
import re
from scipy.sparse import hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from Score import score  

full_set = dict()
with open("Slang_data/dynamic_weighted_en.txt","r") as cens_lang:
    for index,key in enumerate(cens_lang):
        key = key.strip()
        key_new = key.split(',')
        full_set[key_new[0]] = float(key_new[1])    

with open("vulgarity_model.pkl", "rb") as model_file:
    model = joblib.load(model_file)


with open("Slang_data/en.txt", "r") as cens_lang:
    cens_word = {line.strip().lower() for line in cens_lang}


vectorizer = joblib.load("tfidf_vectorizer.pkl")


def censor_text(text, threshold):
    
    
    
    text_list = re.findall(r'\b[A-Za-z0-9]+\b', text.lower())

    
    X_tfidf = vectorizer.transform([" ".join(text_list)])
    
    
    explicit_feature = [[1 if any(word in cens_word for word in text_list) else 0]]

    
    X_combined = hstack((X_tfidf, explicit_feature))

    
    prediction = model.predict(X_combined)[0]

    if prediction == 0:  
        return text  

    
    score_value = score(text, cens_word)

    censored_text_list = []
    for txt in text_list:
        value = full_set.get(txt, 0)  # Get weight, default to 0 if not found
        if value >= threshold:
            censored_text_list.append("[CENSORED]")
        else:
            censored_text_list.append(txt)

    return " ".join(censored_text_list)  # Join words back into a sentence


user_text = input("Enter text: ")
thresh = float(input("enter the input [(high censorship)0.1 - 0.9 (low censorship)] :-"))
print("Processed:", censor_text(user_text,thresh))

