##
##
##

import flet as ft
import requests

from kivy.app import App
from kivy.lang import Builder
from flet import Text, TextField, FilledButton, Row
from datetime import date, datetime


 
def main(pagina: ft.Page):

    pagina.title = "Canivete App by matapato"

    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    pagina.theme_mode = ft.ThemeMode.DARK 

    global temptext2
    global temptext
    temptext = ft.Text("Temperatura: aguardando...")
    global rastrear3
    global rastrear2
    rastrear2 = ft.Text("OBJETO STATUS: aguardando...")
    hora_atual = datetime.now()
    global hora
    hora = hora_atual.strftime('%H:%M:%S')

    def correios(code2):
        
        url = f'https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo={code2}'
        requisition = requests.get(url)
        if requisition.status_code == 429 or requisition.status_code ==  401:
            return(f"{requisition.status_code} - {requisition.text}")
        else:   
            dic_requisition = requisition.json()
            numero = dic_requisition["eventos"][0]["status"]
            return numero
    pagina.update()
  
    def pegar_cotacao(moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao
    
    def temperatura():
        global temptext
        global temptext2
        global hora
        currentTemp = 30.2
        tempHigh = 40.7
        tempLow = -18.9
        if currentTemp > tempLow and currentTemp < tempHigh:
            pagina.remove(temptext2)
            temptext = ft.Text(f"Hoje dia: {date.today()} às {hora} a temperatura atual é: {str(currentTemp)} graus, está entre o extremo alto e extremo baixo")
            temptext2 = ft.Row([temptext], alignment=ft.MainAxisAlignment.CENTER)
            pagina.insert(3,temptext2)
            pagina.update()

    def adicionar2(e):
        global rastrear2
        global rastrear3
        if not caixa_texto.value:
            caixa_texto.error_text = "Digite o código de rastreio"
            pagina.update()
        else:
            temperatura()
            pagina.remove(rastrear3)
            rastrear2 = ft.Text(f"OBJETO STATUS: {correios(caixa_texto.value)}")
            rastrear3 = ft.Row([rastrear2], alignment=ft.MainAxisAlignment.CENTER)
            pagina.insert(1,rastrear3)
            pagina.update()
          

        ### def do botao
            
        ## def chamabotao(o):
        ## temperatura()
        ## adicionar2()
        ## return


    # criar os itens que queremos na página

    botao_add_codigo = ft.ElevatedButton("Procurar", on_click=adicionar2)

    caixa_texto = ft.TextField(label="Aqui vai o codigo", width=250, height=50, text_align=ft.TextAlign.CENTER)

    dolares = ft.Text(f"Dólar R${pegar_cotacao('USD')}")

    # adicinar os itens na página

    rastrear3 = ft.Row([rastrear2], alignment=ft.MainAxisAlignment.CENTER)
    temptext2 = ft.Row([temptext], alignment=ft.MainAxisAlignment.CENTER)

    pagina.add(

    ft.Row([caixa_texto, botao_add_codigo], alignment=ft.MainAxisAlignment.CENTER),
    rastrear3,
    ft.Row([dolares], alignment=ft.MainAxisAlignment.CENTER),
    temptext2
    )

    pagina.update()

ft.app(target=main)
