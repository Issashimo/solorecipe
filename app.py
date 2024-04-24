from flask import Flask, render_template, request
import recommend

app = Flask(__name__)
ingredients = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        ingredients.append(request.form["ingredient"])
        return render_template("register.html", ingredients=ingredients)


@app.route("/recommend")
def recommend():
    import recommend

    recipe = recommend.recommender(ingredients)
    return render_template("recommend.html", recipe=recipe)


if __name__ == "__main__":
    app.run(debug=True)
