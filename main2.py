#!/usr/bin/env python3
# coding:utf-8
import mechanize
from bs4 import BeautifulSoup


def view_page(url, proxy=None):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    user_agent = [("User-agent", "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0")]
    browser.addheaders = user_agent
    url_list = []
    if proxy:
        browser.set_proxies(proxy)
    if url.endswith("/"):
        url = url.rstrip("/")
    page = browser.open(url)
    soup = BeautifulSoup(page, "html.parser")
    for link in soup.find_all("a"):
        l = link.get("href")
        if len(l) > 0 and not l.startswith("#"):
            if l.startswith("/"):
                l = url + l
            if l not in url_list:
                url_list.append(l)
    for link in url_list:
        print(link)
    # for cookie in browser.cookiejar:
    #     print(cookie)
    # print(page.read())


view_page("https://sleyter.net")