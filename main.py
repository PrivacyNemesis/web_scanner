from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import mechanize

def my_ip():
    session = HTMLSession()
    ip_url = "https://www.mon-ip.com/info-adresse-ip.php"
    response = session.get(ip_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ip = soup.find('span', {'id': 'ip4'}).text
    print(f"Votre adresse IP est {ip}")

def get_proxy():
    free_proxy_url = "https://free-proxy-list.net/anonymous-proxy.html"
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
                
                if https == "yes" and last_checked <= "30 secs ago" or last_checked == "1 min ago":
                    print(f"IP: {ip}, Port: {port}, Pays: {country}, Actualisation: {last_checked}")
        else:
            print("Aucun proxy disponible.")
    else:
        print("Echec de la requête vers free-proxy-list.net")

my_ip()
get_proxy()        




