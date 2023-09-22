from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from bs4 import BeautifulSoup
import requests
import mechanize

class ScreenManager(BoxLayout):
    pass

class WebScannerApp(App):
    manager = ObjectProperty(None)
    
    def build(self):
        self.manager = ScreenManager()
        return self.manager

def get_proxy():
    free_proxy_url = "https://free-proxy-list.net/anonymous-proxy.html"
    response = requests.get(free_proxy_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        proxy_table = soup.find('table', {'class': 'table table-striped table-bordered'})

        if proxy_table:
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




WebScannerApp().run