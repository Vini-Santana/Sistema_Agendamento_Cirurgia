import customtkinter

import crud
import conexao

# conexao = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='1234',
#     database='cirurgia',
# )
# cursor = conexao.cursor()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x400")
janela.title("Cadastro")

def clique():
    print("Loggin")
texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)


def button_click_event():
    if read.get() == 1:
        dialog = customtkinter.CTkInputDialog(text="Digite seu email", title="email")
        print("Number:", dialog.get_input())


read = customtkinter.CTkCheckBox(janela, text="Ler", command=button_click_event)
read.pack(padx=10, pady=10)


entry_id = customtkinter.CTkEntry(janela, placeholder_text="ID")
entry_id.pack(padx=10, pady=10)

entry_produto = customtkinter.CTkEntry(janela, placeholder_text="produto")
entry_produto.pack(padx=10, pady=10)

entry_valor = customtkinter.CTkEntry(janela, placeholder_text="valor")
entry_valor.pack(padx=10, pady=10)
def inserir():
    crud.create(entry_produto.get(), entry_valor.get())
    print(entry_produto.get(), entry_valor.get())


botao2 = customtkinter.CTkButton(janela, text="criar", command=inserir)
botao2.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="deletar")
botao.pack(padx=10, pady=10)




# senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
# senha.pack(padx=10, pady=10)

# senha = customtkinter.CTkCheckBox(janela, text="lembrar senha")
# senha.pack(padx=10, pady=10)

janela.mainloop()
conexao.cursor.close()
conexao.conexaov.close()

