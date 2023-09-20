import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import sqlite3

class BackEnd():
    def conectar_db(self):
        self.conn = sqlite3.connect("Sistema_cadastro.db")
        self.cursor = self.conn.cursor()
        print("Banco de dados criado com sucesso!")

    def desconectar_db(self):
        self.conn.close()
        print("Banco de dados desconectado")

    def criar_tabela(self):
        self.conectar_db()
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Usuarios(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirmar_Senha TEXT NOT NULL
            );
        """)
        self.conn.commit()
        print("Tabela craida com sucesso!")
        self.desconectar_db()

    def cadastrar_user(self):
        self.user_cadastro = self.user_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha_cadastro = self.confirma_senha_cadastro_entry.get()

        self.conectar_db()

        self.cursor.execute("""
        INSERT INTO Usuarios (Username, Email, Senha, Confirmar_Senha)
        VALUES (?, ?, ?, ?)""",
        (self.user_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha_cadastro))

        try:
            if(self.user_cadastro == "" or self.email_cadastro == "" or self.senha_cadastro == "" or self.confirma_senha_cadastro == ""):
               messagebox.showerror("Sistema de Login", "Por favor preencha todos os campos.") 
            elif(len(self.user_cadastro) < 4):
                messagebox.showwarning("Sistema de Login", "Nome de Usuario ser de pelo menos 4 caracteres.")
            elif(len(self.senha_cadastro) < 4):
                messagebox.showwarning("Sistema de Login", "A senha deve conter pleo menos 4 caracteres.")
            elif(self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror("Sistema de Login", "A senhas colocadas não são iguais.")
            else:
                self.conn.commit()
                messagebox.showinfo("Sistema de Login", f"Usuario {self.user_cadastro} Cadastrado com Sucesso!")
        except:
            messagebox.showerror("Sistema de Login", "Erro no processamento do seu cadastro!\nPor favor tente novamente.")

class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.config_tela_principal()
        self.tela_login()
        self.criar_tabela()

    # Configuração da tela principal
    def config_tela_principal(self):
        self.geometry("700x400")
        self.title("Sistema de login")
        self.resizable(False, False)
    
    def tela_login(self):
        # Colocando a logo na tela
        self.img = PhotoImage(file="logo.png")
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)

        #Titulo do aplicativo
        self.title = ctk.CTkLabel(self, text="Faça o login ou\ncadastre-se na nossa plataforma!", font=("Century Gothic bold", 14))
        self.title.grid(row=0, column=0, pady=10, padx=10)

        #Criar frame do formulario de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        #Colocando widgets dentro do frame 
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o login", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)
        
        self.user_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Nome de usuario...", font=("Century Gothic bold", 16))
        self.user_login_entry.grid(row=1, column=0, padx=10, pady=10)

        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Senha do usuario...", font=("Century Gothic bold", 16), show="*")
        self.senha_login_entry.grid(row=2, column=0, padx=10, pady=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Mostrar Senha", font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=3, column=0, padx=10, pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="Login", font=("Century Gothic bold", 16), corner_radius=15, fg_color="Green", hover_color="#050")
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)

        self.sap = ctk.CTkLabel(self.frame_login, text="Caso não tenha conta,\nclique no botão abaixo e cadastrar!", font=("Century Gothic", 10))
        self.sap.grid(row=5, column=0, padx=10, pady=10)

        self.btn_registro = ctk.CTkButton(self.frame_login, width=300, text="Registro", font=("Century Gothic bold", 16), corner_radius=15, hover_color="#00008b", command=self.tela_cadastro)
        self.btn_registro.grid(row=6, column=0, padx=10, pady=10)
    
    def tela_cadastro(self):
        #Remover o fomulario de login
        self.frame_login.place_forget()

        #Criando a frame de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)

        #Criando o titulo
        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="Faça o Registro", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        #Criar os widgets da tela de cadastro
        self.user_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Nome de usuario...", font=("Century Gothic bold", 16))
        self.user_cadastro_entry.grid(row=1, column=0, padx=10, pady=5)

        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email do usuario...", font=("Century Gothic bold", 16))
        self.email_cadastro_entry.grid(row=2, column=0, padx=10, pady=5)

        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha do usuario...", font=("Century Gothic bold", 16), show="*")
        self.senha_cadastro_entry.grid(row=3, column=0, padx=10, pady=5)

        self.confirma_senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirmar Senha do usuario...", font=("Century Gothic bold", 16), show="*")
        self.confirma_senha_cadastro_entry.grid(row=4, column=0, padx=10, pady=5)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="Mostrar Senha", font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=5, column=0, padx=10, pady=5)

        self.btn_cadastro = ctk.CTkButton(self.frame_cadastro, width=300, text="Registrar", font=("Century Gothic bold", 16), corner_radius=15, hover_color="#050", command=self.cadastrar_user, fg_color="Green")
        self.btn_cadastro.grid(row=6, column=0, padx=10, pady=5)

        self.btn_login = ctk.CTkButton(self.frame_cadastro, width=300, text="Voltar ao Login", font=("Century Gothic bold", 16), corner_radius=15, command=self.tela_login, hover_color="#00008b")
        self.btn_login.grid(row=7, column=0, padx=10, pady=5)
    
    def limpa_entry_cadastro(self):
        self.user_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.confirma_senha_cadastro_entry.delete(0, END)

    def limpa_entry_login(self):
        self.user_login_entry.delete(0, END)
        self.senha_login_entry.delete(0, END)
        
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = App()
    app.mainloop()