# spelling bee solver

import requests
import json
import re


url = "https://www.nytimes.com/puzzles/spelling-bee"

response = requests.get(url)

js_content = response.text
pattern = r'window.gameData = (.*?)(?=window.gameData|<\/script)'
match = re.search(pattern, js_content, re.DOTALL)

if match:
    json_data = match.group(1)
    data_dict = json.loads(json_data)
    today_data = data_dict.get("today", {})
    today_answers = today_data.get("answers", [])
    today_answers.sort()
    print("The answer for today's Spelling Bee are:")
    for answer in today_answers:
        cstr = answer.capitalize()
        print(cstr.rjust(15, '-'))
else:
    print("Today's data not found.")
