from parsel import Selector
import requests
from time import sleep
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
        sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)

    news_links = selector.css(".cs-overlay-link::attr(href)").getall()

    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_button_link = selector.css(".next.page-numbers::attr(href)").get()

    return next_button_link


def get_summary(first_paragraph):
    summary = ""
    for phrase in first_paragraph:
        summary += phrase
    summary = summary.strip()
    return summary


def get_category(url):
    url_without_http = url.split("//")[1]
    category = url_without_http.split("/")[1]
    category = category.capitalize()
    if category == "Linguagem-de-programacao":
        category = "Linguagem de Programação"
    if category == "Noticias":
        category = "Notícias"

    return category


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("head link[rel='canonical']::attr(href)").get()

    title = selector.css(".entry-title::text").get()
    title = title.strip()

    timestamp = selector.css(".meta-date::text").get()

    writer = selector.css(".url.fn.n::text").get()

    reading_time_text = selector.css(".meta-reading-time::text").get()
    reading_time = int(reading_time_text.split(" ")[0])

    first_paragraph = selector.css(
        ".entry-content>p:first-child *::text"
    ).getall()
    if len(first_paragraph) == 0:
        first_paragraph = selector.css(
            ".entry-content>p:nth-child(2) *::text"
        ).getall()
    summary = get_summary(first_paragraph).strip()

    category = get_category(url)

    dict = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }

    return dict


# Requisito 5
def get_tech_news(amount):
    result = []
    next_page_link = "https://blog.betrybe.com/"
    print("amount", amount)
    while len(result) <= amount:
        response_text = fetch(next_page_link)
        news_links = scrape_updates(response_text)
        for index in range(len(news_links)):
            response_text_aux = fetch(news_links[index])
            content = scrape_news(response_text_aux)
            result.append(content)
            print("len(result)", len(result))
            if len(result) == amount:
                print("break")
                break
        print("while")
        next_page_link = scrape_next_page_link(response_text)

    create_news(result)
    return result
