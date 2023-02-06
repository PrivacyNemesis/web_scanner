import mechanize
from bs4 import BeautifulSoup

def view_page(url):
    browser = mechanize.Browser
    # browser.set_handle_robots(False)
    user_agent = [("user-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15")]
    browser.addheaders = user_agent
    browser.set_proxies({"https": "195.252.219.139:8080"})
    page = browser.open(url)
    for cookie in browser.cookiejar:
        print(cookie)
    print(page.read())
    
view_page("https://sleyter.fr")      