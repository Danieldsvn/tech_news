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


# Requisito 4
def scrape_news(html_content):
    pass


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
