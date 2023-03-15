from tech_news.database import find_news


# Requisito 7
def search_by_title(title):
    result = []
    for content in find_news():
        if title.lower() in content["title"].lower():
            result.append((content["title"], content["url"]))

    print(find_news())
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
