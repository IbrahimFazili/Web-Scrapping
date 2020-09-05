from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import unicodedata

url = 'https://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-' \
      'a-hilarious-response.html/'

response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
questions = content.find_all('h2')

questionsArr = []
for index in range(len(questions)):
    if index > 9:
        questionObject = {
            "question": questions[index].text[4:].encode('utf-8').
            decode('ascii', 'ignore')
        }
    else:
        questionObject = {
            "question": questions[index].text[3:].encode('utf-8').
            decode('ascii', 'ignore')
        }
    questionsArr.append(questionObject)
with open('challengeQuestions.json', 'w') as outfile:
    json.dump(questionsArr, outfile)

df = pd.read_json(r'C:\Users\fazil\OneDrive\Desktop\Projects\Webscraper'
                  r'\challengeQuestions.json')
df.to_csv(r'C:\Users\fazil\OneDrive\Desktop\Projects\Webscraper'
          r'\challengeQuestions.csv', index=None, header=True)
