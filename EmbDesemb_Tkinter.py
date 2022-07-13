#Embaralhar ou desembaralhar uma mensagem.

import tkinter as tk
#from tkinter import *

def criptografar():
    linhas = 4
    mensagem = caixa_mensagem.get()
    while len(mensagem) % linhas != 0 and linhas<=10:
        if linhas >=10:
            mensagem = mensagem+"!"
            linhas = 3
        linhas+=1
    mensagem_trabalhada["text"] = mensagem
    colunas= len(mensagem)/linhas
    colunas= int(colunas)
    i=0
    lista = []
    while i<colunas:
        lista.append(mensagem[i::colunas])
        i+=1
    criptografado=(''.join(lista))
    texto_criptografado["text"]=criptografado
    texto_descriptografado["text"]= ""

def descriptografar():
    linhas= 4
    mensagem = caixa_mensagem.get()
    while len(mensagem) % linhas != 0 and linhas<=10:
        if linhas >=10:
            mensagem = mensagem+"!"
            linhas = 3
        linhas+=1
    mensagem_trabalhada["text"] = mensagem
    colunas= len(mensagem)/linhas
    colunas= int(colunas)
    i=0
    lista = []
    while i<linhas:
        lista.append(mensagem[i::linhas])
        i+=1
    descriptografado = (''.join(lista))
    texto_descriptografado["text"]=descriptografado
    texto_criptografado["text"]=""

janela = tk.Tk()
#janela.geometry("850x250+100+100")
janela.title("Criptografia Simples para Mensagens")
janela.configure(bg = "cyan")

caixa_mensagem = tk.StringVar()
mensagem = caixa_mensagem.get()

texto1 = tk.Label(janela, text = "Digite a mensagem:")
texto1.grid(row=0, column=0, padx=10, pady=10, sticky= "e")
texto1.configure(font = "Arial 15 bold", bg = "cyan")

caixa_entrada = tk.Entry(janela, textvariable=caixa_mensagem, width = 100)
caixa_entrada.grid(row=0, column=1, padx=10, pady=10)
caixa_entrada.configure(font = "Arial 11", bg = "white")

botão1 = tk.Button (janela, text = "Criptografar", command = criptografar)
botão1.grid (row=2, column=0, padx=10, pady=10, sticky="e")
botão1.configure(relief = "groove", border=5, font = "Times 12", bg = "green", fg = "yellow")

botão2 = tk.Button (janela, text = "Descriptografar", command = descriptografar)
botão2.grid(row=3, column=0, padx=10, pady=10, sticky = "e")
botão2.configure(relief = "groove", border=5, font = "Times 12", bg = "green", fg = "yellow")

mensagem_trabalhada = tk.Label(janela, text="",relief="groove", border = 5)
mensagem_trabalhada.grid (row = 1, column = 1, padx=10, pady=10)
mensagem_trabalhada.configure(font = "Arial 10 bold", bg = "magenta")

texto_trabalhado = tk.Label(janela, text="O texto trabalhado é :")
texto_trabalhado.grid(row = 1, column = 0, padx = 10, pady = 10, sticky="e")
texto_trabalhado.configure(font = "Arial 10 bold", bg = "cyan")

texto_criptografado = tk.Label(janela, text="")
texto_criptografado.grid (row = 2, column = 1, padx = 10, pady = 10)
texto_criptografado.configure (font = "Arial 10 italic",width = 100, background = "black", foreground = "white")

texto_descriptografado = tk.Label(janela, text="")
texto_descriptografado.grid (row = 3, column = 1, padx = 10, pady = 10)
texto_descriptografado.configure(font="Arial 10 italic",width = 100, background = "black", foreground = "white")

janela.mainloop()

