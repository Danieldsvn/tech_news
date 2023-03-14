from parsel import Selector
import requests
from time import sleep

# import re


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
    selector = Selector(text=html_content)
    print("selector", selector)

    url = selector.css("head link[rel='canonical']::attr(href)").get()
    print("url -> ", url)

    title = selector.css(".entry-title::text").get()
    date = selector.css(".meta-date::text").get()
    writer = selector.css(".url.fn.n::text").get()
    reading_time_text = selector.css(".meta-reading-time::text").get()
    reading_time_integer = int(reading_time_text.split(" ")[0])
    # summary_complete = selector.css(".entry-content p").get()
    # summary = re.sub("^<.+>$", "", summary_complete)
    # summary = summary_complete.replace("^<.*>$", "")
    print("title -> ", title)
    print("date -> ", date)
    print("writer -> ", writer)
    print("reading_time_integer -> ", reading_time_integer)
    # print("summary -> ", summary)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
