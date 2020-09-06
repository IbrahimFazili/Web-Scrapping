from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import random

url = 'https://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-' \
      'a-hilarious-response.html/'


def randomQuestion(questionsArr):
    index = random.randint(0, len(questionsArr)-1)
    return questionsArr[index]

def emailAlert(question):
    report = {}
    report["value1"] = question['question']
    res = requests.post("https://maker.ifttt.com/trigger/send_joke/with/k"
                        + "ey/jsyYEmFL6d3tocZLGLoMDmdHdPXeFQDaRFD9huXlW-o",
                        data=report)

def main():
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

    question = randomQuestion(questionsArr)

    with open('Ibrahim_Fazili_FullStackChallenge_challengeQuestions.json', 'w') \
            as outfile:
        json.dump(questionsArr, outfile)

    df = pd.read_json(r'C:\Users\fazil\OneDrive\Desktop\Projects\Webscraper'
                      r'\Ibrahim_Fazili_FullStackChallenge_'
                      r'challengeQuestions.json')  # path will need to change
    df.to_csv(r'C:\Users\fazil\OneDrive\Desktop\Projects\Webscraper'
              r'\Ibrahim_Fazili_FullStackChallenge_challengeQuestions.csv',
              index=None, header=True)
# path will need to change
    emailAlert(question)

main()
