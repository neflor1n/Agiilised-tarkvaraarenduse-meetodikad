from flask import Flask, render_template, request, redirect, url_for
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Uudiste allikad ja valmistekstid
news_sources = {
    "Tehnoloogia": ["Uus AI mudel murrab rekordeid", "Startup toob turule nutika prillipaari"],
    "Spordiuudised": ["Eesti jalgpallikoondis võitis 3:1", "Korvpallihooaeg algab suure derbiga"],
    "Majandus": ["Inflatsioon aeglustub", "Uus idufirma kaasas 2 miljonit eurot"]
}

news_list = []

# Genereeri juhuslik kuupäev viimase 7 päeva jooksul
def random_date():
    today = datetime.today()
    days_ago = random.randint(0, 6)
    date = today - timedelta(days=days_ago)
    return date.strftime("%Y-%m-%d")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        category = request.form.get("category")
        if category in news_sources:
            title = random.choice(news_sources[category])
            date = random_date()
            news_list.append({"id": len(news_list), "category": category, "title": title, "date": date})
        return redirect(url_for("index"))
    return render_template("index.html", news_list=news_list, categories=news_sources.keys())

@app.route("/add", methods=["POST"])
def add_news():
    title = request.form.get("title")
    category = request.form.get("category")
    if title and category:
        news_list.append({"id": len(news_list), "category": category, "title": title, "date": random_date()})
    return redirect(url_for("index"))

@app.route("/edit/<int:news_id>", methods=["GET", "POST"])
def edit_news(news_id):
    news = next((item for item in news_list if item["id"] == news_id), None)
    if not news:
        return "Uudis ei leitud", 404
    if request.method == "POST":
        news["title"] = request.form.get("title")
        news["category"] = request.form.get("category")
        return redirect(url_for("index"))
    return render_template("edit.html", news=news, categories=news_sources.keys())

@app.route("/reset")
def reset():
    news_list.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)