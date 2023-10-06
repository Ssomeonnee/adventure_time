from flask import Flask, render_template
app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "Постапокалиптическая Земля", "URL": "/Post-Apocalyptic_Earth" },
    { "title": "Другие измерения и порталы", "URL": "/Other_dimensions" },
    { "title": "Земли Ууу", "URL": "/Lands_OOO" },
    { "title": "Немного истории", "URL": "/Some_history" },
    { "title": "Об авторе", "URL": "/About_athor" },
    { "title": "Глоссарий", "URL": "/Glossary" },
]

@app.context_processor
def global_context():
    return {
    "nav": nav
    }

@app.route("/")
def hello_world():
    return render_template("index.html", name="Главная")

@app.route("/Post-Apocalyptic_Earth")
def about_view():
    return render_template("Post-Apocalyptic_Earth.html", name="Постапокалиптическая Земля")

@app.route("/Other_dimensions")
def best_page_view():
    return render_template("Other_dimensions.html", name="Другие измерения и порталы")

@app.route("/Lands_OOO")
def Lands_OOO_view():
    return render_template("Lands_OOO.html", name="Земли Ууу")

@app.route("/Some_history")
def Some_history_view():
    return render_template("Some_history.html", name="Немного истории")

@app.route("/About_athor")
def About_athor_view():
    return render_template("About_athor.html", name="Об авторе")

@app.route("/Glossary")
def Glossary_view():
    return render_template("Glossary.html", name="Глоссарий")