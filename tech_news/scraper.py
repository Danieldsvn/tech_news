from parsel import Selector
import requests
from time import sleep


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
    if category == "linguagem-de-programacao":
        category = "Linguagem de Programação"
    if category == "noticias":
        category = "Notícias"

    return category.capitalize()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("head link[rel='canonical']::attr(href)").get()
    print("url -> ", url)

    title = selector.css(".entry-title::text").get()
    title = title.strip()
    print("title -> ", title)

    timestamp = selector.css(".meta-date::text").get()
    print("timestamp -> ", timestamp)

    writer = selector.css(".url.fn.n::text").get()
    print("writer -> ", writer)

    reading_time_text = selector.css(".meta-reading-time::text").get()
    reading_time = int(reading_time_text.split(" ")[0])
    print("reading_time -> ", reading_time)

    first_paragraph2 = selector.css(".entry-content>p:first-child").getall()
    print("first_paragraph2", first_paragraph2)

    first_paragraph = selector.css(
        ".entry-content>p:first-child *::text"
    ).getall()
    print("first_paragraph", first_paragraph)
    summary = get_summary(first_paragraph).strip()
    print("summary -> ", summary)

    category = get_category(url)
    print("category -> ", category)

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
    """Seu código deve vir aqui"""
