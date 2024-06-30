import requests
import json
import time
import pandas as pd
from pandas import json_normalize
from pprint import pprint

# 1. 楽天レシピのレシピカテゴリ一覧を取得する

def ID():
    res = requests.get("https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId=1080534497721355158")

    json_data = json.loads(res.text)

    parent_dict = {}  # mediumカテゴリの親カテゴリの辞書

    df = pd.DataFrame(columns=["category1", "category2", "category3", "categoryId", "categoryName"])

    for category in json_data["result"]["large"]:
        df = df._append(
            {
                "category1": category["categoryId"],
                "category2": "",
                "category3": "",
                "categoryId": category["categoryId"],
                "categoryName": category["categoryName"],
            },
            ignore_index=True,
        )

    for category in json_data["result"]["medium"]:
        df = df._append(
            {
                "category1": category["parentCategoryId"],
                "category2": category["categoryId"],
                "category3": "",
                "categoryId": str(category["parentCategoryId"])
                + "-"
                + str(category["categoryId"]),
                "categoryName": category["categoryName"],
            },
            ignore_index=True,
        )
        parent_dict[str(category["categoryId"])] = category["parentCategoryId"]

    for category in json_data["result"]["small"]:
        df = df._append(
            {
                "category1": parent_dict[category["parentCategoryId"]],
                "category2": category["parentCategoryId"],
                "category3": category["categoryId"],
                "categoryId": parent_dict[category["parentCategoryId"]]
                + "-"
                + str(category["parentCategoryId"])
                + "-"
                + str(category["categoryId"]),
                "categoryName": category["categoryName"],
            },
            ignore_index=True,
        )

# 2. キーワードからカテゴリを抽出する
    df_keyword = df["categoryId"]
    
    return df_keyword
