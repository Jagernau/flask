from flask import Flask
from json import load

with open("candidates.json", encoding="utf-8") as f:
    names = load(f)

app = Flask(__name__)

@app.route("/")
def page_index():
    return "Главная страничка"
   
@app.route("/prof/<uid>")
def page_prof(uid):
    return f"Профиль {uid}"

app.run()
