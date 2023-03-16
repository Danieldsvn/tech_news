from tech_news.database import find_news


# Requisito 7
def search_by_title(title):
    result = []
    for content in find_news():
        if title.lower() in content["title"].lower():
            result.append((content["title"], content["url"]))

    return result


def is_date_iso_format(date: str):
    date_splited = date.split("-")
    if len(date_splited) != 3:
        raise ValueError("Data inválida")
    year, month, day = date_splited
    if len(year) != 4 or len(month) != 2 or len(month) != 2:
        raise ValueError("Data inválida")
    year = int(year)
    month = int(month)
    day = int(day)
    is_date_valid(year, month, day)
    year, month, day = date.split("-")
    date_formated = f"{day}/{month}/{year}"
    return date_formated


def is_date_valid(year, month, day):
    if year < 0 or month > 12 or day > 31:
        raise ValueError("Data inválida")
    if month == 2 and day > 29:
        raise ValueError("Data inválida")
    return None


# Requisito 8
def search_by_date(date):
    try:
        date_formated = is_date_iso_format(date)
        result = []
        for content in find_news():
            if date_formated == content["timestamp"]:
                result.append((content["title"], content["url"]))
        return result
    except ValueError as error:
        print(error)
        raise


# Requisito 9
def search_by_category(category):
    result = []
    for content in find_news():
        if category.lower() in content["category"].lower():
            result.append((content["title"], content["url"]))

    return result
