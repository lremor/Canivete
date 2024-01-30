##
##
##

import flet as ft
import requests

from flet import Text, TextField, FilledButton, Row
from datetime import date, datetime


 
def main(pagina: ft.Page):

    pagina.title = "Canivete App by matapato"

    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    pagina.theme_mode = ft.ThemeMode.DARK 

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
    
    def flight():
        url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"
        querystring = {"fromId":"XAP.AIRPORT","toId":"GRU.AIRPORT","departDate":"2024-12-12","stops":"0", "pageNo":"1","adults":"2","children":"0","currency_code":"BRL"}
        headers = {
	        "X-RapidAPI-Key": "48bbb58dfdmshb1718674f5b879ap105aaajsn5936fc8b7282",
	        "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 429 or response.status_code ==  401:
            return(f'  ERRO: {response.status_code} -\n {response.text}')
        else:   
            flight_requisition = response.json()
            flight_valor = flight_requisition["data"]["flightDeals"][0]["price"]["units"]
            return flight_valor

    def temperatura():
        global hora
        urltemp = "https://open-weather13.p.rapidapi.com/city/erechim,%20brazil"
        headerstemp = {
	        "X-RapidAPI-Key": "48bbb58dfdmshb1718674f5b879ap105aaajsn5936fc8b7282",
	        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
        }
        response2 = requests.get(urltemp, headers=headerstemp)
        temp_requisition = response2.json()
        temp_valor = temp_requisition["main"]["temp"]
        F = float(temp_valor)
        C = (F - 32) * (5 / 9)
        temp_C = int(C)
        return temp_C
        
    def adicionar2(e):
        global rastrear2
        global rastrear3
        if not caixa_texto.value:
            caixa_texto.error_text = "Digite o código de rastreio"
            pagina.update()
        else:
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

    botao_add_codigo = ft.ElevatedButton('Procurar', on_click=adicionar2)

    caixa_texto = ft.TextField(label='Aqui vai o codigo', width=250, height=50, text_align=ft.TextAlign.CENTER)

    dolares = ft.Text(f'Dólar R${pegar_cotacao('USD')}')

    flight_txt = ft.Text(f'O valor do voo para o dia 21/12/2024 (2 pessoas) está em R${flight()}')

    temp_txt = ft.Text(f'Hoje dia: {date.today()} às {hora} a temperatura atual é: {temperatura()}° graus!')

    # adicinar os itens na página

    rastrear3 = ft.Row([rastrear2], alignment=ft.MainAxisAlignment.CENTER)
    temp_txt2 = ft.Row([temp_txt], alignment=ft.MainAxisAlignment.CENTER)

    pagina.add(

    ft.Row([caixa_texto, botao_add_codigo], alignment=ft.MainAxisAlignment.CENTER),
    rastrear3,
    ft.Row([dolares], alignment=ft.MainAxisAlignment.CENTER),
    temp_txt2,
    ft.Row([flight_txt], alignment=ft.MainAxisAlignment.CENTER)
    )

    pagina.update()

ft.app(target=main)
