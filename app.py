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


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    import recommend

    recipe = recommend.recommender(ingredients)

    if request.method == "GET":
        return render_template(
            "recommend.html",
            Id1=recipe[0][1],
            title1=recipe[0][2],
            photo1=recipe[0][3],
            Id2=recipe[1][1],
            title2=recipe[1][2],
            photo2=recipe[1][3],
            Id3=recipe[2][1],
            title3=recipe[2][2],
            photo3=recipe[2][3],
            Id4=recipe[3][1],
            title4=recipe[3][2],
            photo4=recipe[3][3],
            Id5=recipe[4][1],
            title5=recipe[4][2],
            photo5=recipe[4][3],
            Id6=recipe[5][1],
            title6=recipe[5][2],
            photo6=recipe[5][3],
        )


@app.route("/loading", methods=["GET", "POST"])
def loading():
    with open("data/alternate.txt") as f:
        l = []
        explanation = []
        judge = True
        while judge == True:
            e = f.readline()
            if e == "":
                break
            e_ = list(e.split(","))
            print(e_[0])
            l.append(e_[0])
            explanation.append(e_[1])
        print(l)
        print(explanation)

    if request.method == "POST":
        Id = request.form["Id"]
        photo = request.form["photo"]
        title = request.form["title"]
        import material

        materials, amounts = material.page(Id)
        ingredient = []
        explanations = []
        for i in range(len(l)):
            if str(l[i]) in materials:
                ingredient.append(l[i])
                explanations.append(explanation[i])

        url = "https://recipe.rakuten.co.jp/recipe/" + str(Id) + "/"

        return render_template(
            "recommend_recipe.html",
            material=materials,
            amount=amounts,
            Id=Id,
            photo=photo,
            title=title,
            url=url,
            ingredient=ingredient,
            explanation=explanations,
        )


@app.route("/member_register")
def member_register():
    return render_template("member_register.html")


@app.route("/member_login")
def member_login():
    return render_template("member_login.html")


if __name__ == "__main__":
    app.run(debug=True)
