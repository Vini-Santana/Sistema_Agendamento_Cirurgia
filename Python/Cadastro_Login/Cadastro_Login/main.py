import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from validacao import validaUsuarioSenha_RetornaNivelAcesso
from crud import createPerfilDeAcesso

def tela_registro():
    frame.pack_forget()

    registro_frame = ctk.CTkFrame(tela, width=350, height=396)
    registro_frame.pack(side=RIGHT)

    label = ctk.CTkLabel(registro_frame, text="Faça seu cadastro", font=("Roboto",25,'bold'), text_color=('white'))
    label.place(x=75, y=40)

    login_entry = ctk.CTkEntry(registro_frame, placeholder_text="Nome do Usuario", width=300, font=("Roboto", 14))
    login_entry.place(x=25, y=105)

    pass_entry = ctk.CTkEntry(registro_frame, placeholder_text="Senha do Usuario", width=300, font=("Roboto", 14))
    pass_entry.place(x=25, y=150)

    cpass_entry = ctk.CTkEntry(registro_frame, placeholder_text="Confirmar Senha do Usuario", width=300, font=("Roboto", 14))
    cpass_entry.place(x=25, y=195)

    opcoes = ["Adm", "Comum"]
    selected_option = ctk.StringVar()

    combo = ctk.CTkComboBox(registro_frame, variable=selected_option, values=opcoes)
    combo.place(x=25, y=235)
    combo.set(opcoes[0])

    cheekbook_rg = ctk.CTkCheckBox(registro_frame, text="Aceito os termos e condições para registro")
    cheekbook_rg.place(x=25, y=280)

    def voltar_login():
        registro_frame.pack_forget()

        frame.pack(side=RIGHT)

    voltar_button = ctk.CTkButton(registro_frame, text="VOLTAR", width=150, fg_color="gray", hover_color="#61727C", command=voltar_login)
    voltar_button.place(x=25, y=330)

    def salvar_user():
        usuario = login_entry.get()
        senha = pass_entry.get()
        confirma_senha = cpass_entry.get()
        nivel_acesso = selected_option.get()

        if senha != confirma_senha:
            messagebox.showerror(title="Erro no Registro", message="As senhas não coincidem")
            return
        
        # Mapeia o valor da combobox para o valor correspondente no banco de dados
        if nivel_acesso == "Adm":
            nivel_acesso = "1"
        elif nivel_acesso == "Comum":
            nivel_acesso = "2"
        
        try:
            createPerfilDeAcesso(senha, usuario, nivel_acesso)
            messagebox.showinfo(title="Estado do Cadastro", message="Usuário Registrado com sucesso")
        except Exception as e:
            messagebox.showerror(title="Erro no Registro", message=str(e))

    registrar_button = ctk.CTkButton(registro_frame, text="REGISTRAR", width=150, command=salvar_user)
    registrar_button.place(x=180, y=330)

def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    try:
        nivel_acesso = validaUsuarioSenha_RetornaNivelAcesso(usuario, senha)
        msg = messagebox.showinfo(title="Estado de Login", message="Usuário Logado com sucesso")
        # Faça algo com o nível de acesso, se necessário
        print("Nível de Acesso:", nivel_acesso)
    except ValueError as e:
        # Se houver um erro de validação, exiba uma mensagem de erro
        msg = messagebox.showerror(title="Erro de Login", message=str(e))

# Tela
# Setando o tema escuro na tela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Criando o tamanho e colocando o icone 
tela = ctk.CTk()
tela.geometry("700x400")
tela.title("Sistema Cirurgia")
tela.iconbitmap("icone.ico")
tela.resizable(False, False)

# Colocando foto na tela
img = PhotoImage(file="cirurgia.png")
nova_img = img.subsample(2)
label_img = ctk.CTkLabel(tela, image=nova_img, text="")
label_img.place(x=5, y=65)

label_tt = ctk.CTkLabel(tela, text="Entre na sua conta e \ntenha acesso a plataforma", font=("Roboto", 20, 'bold'), text_color="#00B0F0")
label_tt.place(x=25, y=5)

#frame
frame = ctk.CTkFrame(tela, width=350, height=396)
frame.pack(side=RIGHT)

#Frame widgets
label = ctk.CTkLabel(frame, text="Sistema de login", font=("Roboto",25,'bold'), text_color=('white'))
label.place(x=75, y=55)

entry_usuario = ctk.CTkEntry(frame, placeholder_text="Nome do Usuario", width=300, font=("Roboto", 14))
entry_usuario.place(x=25, y=105)

label_campo_usu = ctk.CTkLabel(frame, text="*O campo nome do usuario é obrigatóro", text_color="red", font=("Roboto", 12))
label_campo_usu.place(x=25, y=135)

entry_senha = ctk.CTkEntry(frame, placeholder_text="Senha do Usuario", width=300, font=("Roboto", 14), show="*")
entry_senha.place(x=25, y=165)

label_campo_senha = ctk.CTkLabel(frame, text="*O campo senha do usuario é obrigatóro", text_color="red", font=("Roboto", 12))
label_campo_senha.place(x=25, y=195)

cheekbox = ctk.CTkCheckBox(frame, text="Monstrar senha")
cheekbox.place(x=25, y=230)

button_login = ctk.CTkButton(frame, text="LOGIN", font=("Roboto", 14),width=300, fg_color="#8C1F28" ,hover_color="#1C646D", command=login)
button_login.place(x=25, y=280)

registro_span = ctk.CTkLabel(frame, text="Senão houver conta ->").place(x=25, y=320)
button_registro = ctk.CTkButton(frame, text="REGISTRO", font=("Roboto", 14),width=150, hover_color="green", command=tela_registro)
button_registro.place(x=170, y=320)


tela.mainloop()