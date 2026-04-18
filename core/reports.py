from core.storage import load_expenses


def get_monthly_totals():
    rows = load_expenses()
    totals = {}

    for row in rows:
        month = row["date"][:7]
        totals[month] = totals.get(month, 0) + float(row["amount"])

    return totals


def get_category_totals():
    rows = load_expenses()
    totals = {}

    for row in rows:
        cat = row["category"]
        totals[cat] = totals.get(cat, 0) + float(row["amount"])

    return totals