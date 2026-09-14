from flask import Flask, render_template

app = Flask(__name__)


# =========================
# MAIN HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# GAME PAGE
# =========================

@app.route("/game")
def game():
    return render_template("game.html")


# =========================
# MAIN GAME MAP
# =========================

@app.route("/map")
def game_map():
    return render_template("map.html")


# =========================
# ANCIENT INDIA
# =========================

@app.route("/ancient-india")
def ancient_india():
    return render_template("ancient_india.html")


# =========================
# GREAT KINGDOMS
# =========================

@app.route("/great-kingdoms")
def great_kingdoms():
    return render_template("great_kingdoms.html")


# =========================
# FREEDOM QUEST
# =========================

@app.route("/freedom-quest")
def freedom_quest():
    return render_template("freedom_quest.html")


# =========================
# CULTURE EXPLORER
# =========================

@app.route("/culture-explorer")
def culture_explorer():
    return render_template("culture_explorer.html")


# =========================
# FESTIVAL CHALLENGE
# =========================

@app.route("/festival-challenge")
def festival_challenge():
    return render_template("festival_challenge.html")


# =========================
# MONUMENT MYSTERY
# =========================

@app.route("/monument-mystery")
def monument_mystery():
    return render_template("monument_mystery.html")


# =========================
# RUN FLASK APPLICATION
# =========================

if __name__ == "__main__":
    app.run(debug=True)