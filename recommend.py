def recommender(ingredients):
    import openpyxl
    import alternate

    ingredients = alternate.alternate(ingredients)

    write_wb = openpyxl.load_workbook("data/recipe.xlsx")
    write_ws = write_wb["Sheet1"]
    scores = {}

    for i in range(write_ws.max_row):
        j = 0
        score = 0
        while True:
            if write_ws.cell(row=i + 1, column=4 + j).value in ingredients:
                score += 1
                j += 1
            elif write_ws.cell(row=i + 1, column=4 + j).value == None:
                break
            else:
                pass
                j += 1

        try:
            scores[write_ws.cell(row=i + 1, column=3).value] = score / j

        except:
            scores[write_ws.cell(row=i + 1, column=3).value] = 0

    scores_sorted = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    result = []
    for i in range(5):
        result.append(scores_sorted[i])

    return result
