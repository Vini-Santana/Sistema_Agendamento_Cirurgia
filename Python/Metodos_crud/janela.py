import customtkinter
from tkinter import messagebox
import crud
import conexao
from datetime import datetime

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
janela = customtkinter.CTk()
janela.geometry("500x400")
janela.title("Cadastro")

#EXEMPLO DE INSERÇÃO NA TABELA TIPO DATETIME
entry_valor_DataInicio = customtkinter.CTkEntry(janela, placeholder_text="dataInicio")
entry_valor_DataInicio.pack(padx=10, pady=10)
entry_valor_DataFim = customtkinter.CTkEntry(janela, placeholder_text="dataFim")
entry_valor_DataFim.pack(padx=10, pady=10)
def inserirTesteData():
    if crud.validaParametroEntreDtInicioDtfimCom(datetime.strptime(entry_valor_DataInicio.get(), '%d/%m/%Y %H:%M:%S'), datetime.strptime(entry_valor_DataFim.get(), '%d/%m/%Y %H:%M:%S')) == "AAAAAAAAAAAAAAAA":
        print("DEU BOM!!")
        crud.createTesteData(datetime.strptime(entry_valor_DataInicio.get(), '%d/%m/%Y %H:%M:%S'), datetime.strptime(entry_valor_DataFim.get(), '%d/%m/%Y %H:%M:%S'))
    else:
        print("ERROOOOOOOOOOOOOOOOOOOOOOOOOO")
botao2 = customtkinter.CTkButton(janela, text="criarData", command=inserirTesteData)
botao2.pack(padx=10, pady=10)


#EXEMPLO DE EXCEÇÃO - ABRE ALERTA DO TKINTER
entry_valor_ESPECIALIZACAO = customtkinter.CTkEntry(janela, placeholder_text="ESPECIALIZAÇÃO")
entry_valor_ESPECIALIZACAO.pack(padx=10, pady=10)
def inserirEspecializacao():
    try:
        crud.createEspecializacao(entry_valor_ESPECIALIZACAO.get())
    except conexao.mysql.connector.errors.IntegrityError as error:
       messagebox.showinfo("cuidado", "AAAAAAAAA")
botao = customtkinter.CTkButton(janela, text="exemplo exception", command=inserirEspecializacao)
botao.pack(padx=10, pady=10)

janela.mainloop()
conexao.cursor.close()
conexao.conexaov.close()
