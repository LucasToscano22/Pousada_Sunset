import os
import json
import socket
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from threading import Thread
from pathlib import Path


#Configuração do cliente

HOST = '127.0.0.1'
PORT = 5000

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((HOST, PORT))


def enviar_mensagem():

    nome = cliente_nome.get()
    email = cliente_email.get()
    pagamento = combobox_selecionarpagamento.get()
    quarto = combobox_selecionarquarto.get()
    data_inicio = calendario_reservainicio.get()
    data_fim = calendario_reservafim.get()

    if not nome or not email or not pagamento:
     label_receber['text'] = "Preencha todos os campos antes de enviar!"


    dados_reserva = {
        'nome': nome,
        'email': email,
        'pagamento': pagamento,
        'quarto': quarto,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'ERRO-802': 'Data não disponível',
        'RESERVA-215': 'Reserva realizada com sucesso'
    }


    mensagem = json.dumps(dados_reserva)
    cliente_socket.sendall(mensagem.encode())

    resposta = cliente_socket.recv(1024).decode()
    label_receber['text'] = resposta
    
    cliente_nome.delete(0, tk.END)
    cliente_email.delete(0, tk.END)
    

with open( '/home/leidiana/Documentos/pousada/lista.json','r') as rel_quartos:
    dic_quartos = json.load(rel_quartos)

quartos = list(dic_quartos.keys())

with open('/home/leidiana/Documentos/pousada/pagamento.json', 'r') as met_pagamento:
    dic_pagamento = json.load(met_pagamento)

metodos_pagamento = list(dic_pagamento.keys())

def buscar_informacao():
    acomodacoes = combobox_selecionarquarto.get()
    
    if acomodacoes == '':
        label_descricao['text'] = message_info['ERR0-800']
    else:
        with open('/home/leidiana/Documentos/pousada/lista.json', 'r') as acomodacao:
            room = json.load(acomodacao)
            info_room = room[acomodacoes]['descricao']
            label_descricao['text'] = f'O quarto possui: \n {info_room}'


def total_pagar():
    quarto = combobox_selecionarquarto.get()
    inicio = calendario_reservainicio.get()
    fim = calendario_reservafim.get()
        
    formato_data = "%d/%m/%Y"
    data_inicio = datetime.strptime(inicio, formato_data)
    data_fim = datetime.strptime(fim, formato_data)
    diferenca_dias = (data_fim - data_inicio).days

    if quarto == '':
        label_valor['text'] = message_info['ERR0-800']

    with open ('/home/leidiana/Documentos/pousada/lista.json','r') as valor:
     valor1 = json.load(valor)
     valor_total = diferenca_dias * valor1[quarto]['preco']


    if diferenca_dias <= 0:
        label_valor['text'] = message_info['ERRO-801']

    else:
        label_valor['text'] = f'Valor total para {diferenca_dias} diárias no quarto {quarto}: \n R$ {valor_total:.2f}'



cliente_nome = None
cliente_email = None
combobox_selecionarpagamento = None

def cliente_reserva():
    
    global cliente_nome, cliente_email, combobox_selecionarpagamento

    quarto = combobox_selecionarquarto.get()

    if quarto == '':
        label_valor['text'] = message_info['ERR0-800']

    label_nome = tk.Label(text = ' Digite seu nome ', anchor='w')
    label_nome.grid(row=9, column=3, padx=10, pady=10, sticky='nsew', columnspan=3)

    cliente_nome = tk.Entry(janela)
    cliente_nome.grid(row=9, column=4, padx=10, pady=10, sticky='nsew', columnspan=4)

    label_email = tk.Label(text = ' Digite seu e-mail ', anchor='w')
    label_email.grid(row=10, column=3, padx=10, pady=10, sticky='nsew', columnspan=3)

    cliente_email = tk.Entry(janela)
    cliente_email.grid(row=10, column=4, padx=10, pady=10, sticky='nsew', columnspan=4)

    label_pagamento = tk.Label(text = ' Forma de Pagamento ', anchor='w')
    label_pagamento.grid(row=11, column=3, padx=10, pady=10, sticky='nsew', columnspan=2)

    combobox_selecionarpagamento = ttk.Combobox(janela, values=metodos_pagamento)
    combobox_selecionarpagamento.grid(row=11,column=4, padx=25, pady=10, sticky='nsew')

    botao_enviar = tk.Button(text="Enviar", command=enviar_mensagem)
    botao_enviar.grid(row=12, column=3, padx=10, pady=10, sticky='nsew')

message_info = {
    'ERR0-800': 'Selecione uma opção de acomodação.',
    'ERRO-801': 'A data final deve ser posterior à data de início.',
    'ERRO-802': 'Data não disponível',
    'RESERVA-215': 'Reserva realizada com sucesso'
}


janela = tk.Tk()

janela.title('Pousada SunSet')

label_pousada = tk.Label(
    text = 'Pousada SunSet', 
    borderwidth=2, 
    background= 'white', 
    width= 12, 
    height= 2,
    foreground= 'blue', 
    relief='solid',
    font=('Helvetica', 32))

label_pousada.grid(row=0, column=0, padx=10, pady=10, sticky='nsew', columnspan=5)

label_acomodacao = tk.Label(text = ' Acomodação ', borderwidth=1, relief='solid', font=('Helvetica', 12))
label_acomodacao.grid(row=1, column=1, padx=10, pady=10, sticky='nsew', columnspan=2)

label_descricao = tk.Label(text='', font=('Helvetica', 11))
label_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=4)

label_reserva = tk.Label(text = ' Reservas ', borderwidth=1, relief='solid', font=('Helvetica', 12))
label_reserva.grid(row=3, column=3, padx=10, pady=10, sticky='nsew', columnspan=3)

label_datainicial = tk.Label(text = ' Data Inicial ', anchor='w', font=('Helvetica', 11))
label_datainicial.grid(row=4, column=3, padx=10, pady=10, sticky='nsew', columnspan=3)

label_datafinal = tk.Label(text = ' Data Final ', font=('Helvetica', 11), anchor='w')
label_datafinal.grid(row=5, column=3, padx=10, pady=10, sticky='nsew', columnspan=3)


label_valor = tk.Label(text='', font=('Helvetica', 11))
label_valor.grid(row=8, column=2, padx=10, pady=10, sticky='nsew', columnspan=3)


label_descricao = tk.Label(text='', font=('Helvetica', 11),anchor="center")
label_descricao.grid(row=2, column=1, padx=10, pady=10, sticky='nsew', columnspan=4)


label_receber = tk.Label(text='')
label_receber.grid(row=12, column=4, padx=10, pady=10, sticky='nsew', columnspan=4)

combobox_selecionarquarto = ttk.Combobox(janela, values=quartos)
combobox_selecionarquarto.grid(row=1,column=3, padx=10, pady=10, sticky='nsew')


botao_informacoes = tk.Button(text="Informações", command=buscar_informacao, font=('Helvetica', 11))
botao_informacoes.grid(row=1, column=4, padx=10, pady=10, sticky='nsew')


botao_valor = tk.Button(text="Valor Total", command=total_pagar)
botao_valor.grid(row=7, column=3, padx=10, pady=10, sticky='nsew')

botao_reservar = tk.Button(text="Reservar", command=cliente_reserva, font=('Helvetica', 11))
botao_reservar.grid(row=9, column=3, padx=10, pady=10, sticky='nsew')

calendario_reservainicio = DateEntry(year=2024, locale='pt_br')
calendario_reservainicio.grid(row=4,column=4, padx=10, pady=10, sticky='nsew')

calendario_reservafim = DateEntry(year=2024, locale='pt_br')
calendario_reservafim.grid(row=5,column=4, padx=10, pady=10, sticky='nsew')



janela.mainloop()

cliente_socket.close()










