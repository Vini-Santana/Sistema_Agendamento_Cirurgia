import customtkinter
import crud
import conexao

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x400")
janela.title("Cadastro")

#CAMPOS PARA INSERIR UM PRODUTO NO BANCO
entry_id = customtkinter.CTkEntry(janela, placeholder_text="ID")
entry_id.pack(padx=10, pady=10)

entry_produto = customtkinter.CTkEntry(janela, placeholder_text="produto")
entry_produto.pack(padx=10, pady=10)

entry_valor = customtkinter.CTkEntry(janela, placeholder_text="valor")
entry_valor.pack(padx=10, pady=10)
def inserir():
    #print(entry_produto.get(), entry_valor.get())
    crud.create(entry_produto.get(), entry_valor.get())

botao2 = customtkinter.CTkButton(janela, text="criar", command=inserir)
botao2.pack(padx=10, pady=10)

#INSERINDO NA TABELA DO TIPO DATE
entry_valor_Data = customtkinter.CTkEntry(janela, placeholder_text="data")
entry_valor_Data.pack(padx=10, pady=10)

def inserirTesteData():
    #print(entry_id.get(), entry_valor_Data.get())
    crud.createTesteData(entry_id.get(), entry_valor_Data.get())

botao2 = customtkinter.CTkButton(janela, text="criarData", command=inserirTesteData)
botao2.pack(padx=10, pady=10)


botao = customtkinter.CTkButton(janela, text="deletar")
botao.pack(padx=10, pady=10)


janela.mainloop()
conexao.cursor.close()
conexao.conexaov.close()
