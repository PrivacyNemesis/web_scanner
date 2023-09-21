import requests
import mechanize
from bs4 import BeautifulSoup

def get_proxy():
    free_proxy = "https://free-proxy-list.net/anonymous-proxy.html"
    check_proxy = requests.get(free_proxy)
    print(check_proxy.status_code)
    
    soup = BeautifulSoup(check_proxy.text, "html.parser")
    list = soup.find_all('table', class_='table table-striped table-bordered')
    
    for proxy in list:
        ip = proxy.find_all('td')[0].text
        port = proxy.find_all('td')[1].text
        code = proxy.find_all('td')[2].text
        country = proxy.find_all('td')[3].text
        anonymity = proxy.find_all('td')[4].text
        google = proxy.find_all('td')[5].text
        https = proxy.find_all('td')[6].text
        last_checked = proxy.find_all('td')[7].text
    print(ip, port, code, country, anonymity, google, https, last_checked)
    
get_proxy()    

