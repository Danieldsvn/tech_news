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
        raise ValueError
    year, month, day = date_splited
    if len(year) != 4 or len(month) != 2 or len(month) != 2:
        raise ValueError
    year = int(year)
    month = int(month)
    day = int(day)
    is_date_valid(year, month, day)


def is_date_valid(year, month, day):
    if year < 0 or month > 12 or day > 31:
        raise ValueError


# Requisito 8
def search_by_date(date):
    print(find_news())


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
