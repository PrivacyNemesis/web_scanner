# coding:utf-8
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import mechanize
import random

def my_ip():
    session = HTMLSession()
    ip_url = "https://www.mon-ip.com/info-adresse-ip.php"
    response = session.get(ip_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ip = soup.find('span', {'id': 'ip4'}).text
    print(f"Votre adresse IP est {ip}")
    
my_ip()
    
def get_proxy():
    free_proxy_url = "https://free-proxy-list.net/"
    response = requests.get(free_proxy_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        proxy_table = soup.find('table', {'class': 'table table-striped table-bordered'})

        if proxy_table:
            print("====================== LISTE DE PROXY DISPONIBLES: ======================")
            rows = proxy_table.find_all('tr')[1:]
            for row in rows:
                columns = row.find_all('td')
                ip = columns[0].text
                port = columns[1].text
                country = columns[3].text
                https = columns[6].text
                last_checked = columns[7].text
                
                if https == "yes" and last_checked <= "30 secs ago":
                    print(f"IP: {ip}, Port: {port}, Pays: {country}, Actualisation: {last_checked}")
        else:
            print("Aucun proxy disponible.")
    else:
        print("Echec de la requête vers free-proxy-list.net")
    return ip, port           


def target(url,):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    user_agent = [("User-agent", "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0")]
    browser.addheaders = user_agent
    url_list = []
    ip, port = random.choice(get_proxy())[:2]
    browser.set_proxies({"https": f"{ip}:{port}"})
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


target("https://cyberini.com")


