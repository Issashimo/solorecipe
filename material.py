from bs4 import BeautifulSoup
import requests


def page(Id):
    materials = []
    amounts = []

    url = "https://recipe.rakuten.co.jp/recipe/" + str(Id) + "/"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    material = soup.find_all(class_="recipe_material__item_name")
    amount = soup.find_all(class_="recipe_material__item_serving")

    for i in material:

        materials.append(i.text)

    for j in amount:

        amounts.append(j.text)

    return materials, amounts


