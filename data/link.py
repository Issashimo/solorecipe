from bs4 import BeautifulSoup
import requests
import openpyxl


def link(url):
    # url = "https://cookpad.com/category/10"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.find_all("a", href=True, class_="recipe-title")

    answer = []

    for i in title:
        answer.append(i["href"])

    return answer


if __name__ == "__main__":
    link()
