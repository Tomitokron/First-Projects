import json
import json.tool

points = 0

with open("quiz.json") as json_file:
    questions = (json.load(json_file))

    print(questions)