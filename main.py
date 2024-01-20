# importar o App
# # criar app
# # criar a funcao build

from kivy.app import App
from kivy.lang import Builder

import requests

GUI = Builder.load_file("tela.kv")

class Canivete(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["temp"].text = "Temperatura"
        self.root.ids["dolar"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["logo1"].text = "Canivete App by matapato"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

Canivete().run()
