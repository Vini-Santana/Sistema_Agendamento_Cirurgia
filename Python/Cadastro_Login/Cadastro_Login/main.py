import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

from crud import createPerfilDeAcesso, obter_tipos_de_cirurgias, obter_salas, obter_cirurgiao, obter_anestesista, obter_instrumentador, buscar_enfermeiros
from validacoes import validaUsuarioSenha_RetornaNivelAcesso, validaDtinicioMenorDtfim, validaHorario

# Criação de outras telas e funções


def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    nivel_acesso = validaUsuarioSenha_RetornaNivelAcesso(usuario, senha)

    if nivel_acesso == 1:
        tela_administrador()
    elif nivel_acesso == 2:   
        tela_comum()
    else:
        messagebox.showerror(title="Erro no login", message="Credenciais inválidas")

def mostrar_senha():
    if show_password_var.get():
        entry_senha.configure(show="")
    else:
        entry_senha.configure(show="*")

def tela_administrador():

    def formatar_horario(event):
        entry_data_inicio = event.widget
        s = entry_data_inicio.get()

        if len(s) == 2 and s.count(':') == 0:
            entry_data_inicio.insert(ctk.END, ':')

        if len(s) > 5:
            entry_data_inicio.delete(5, ctk.END)
    
    def validarhora():
        horario_inicio = entry_horario_inicio.get()
        horario_final = entry_data_fim.get()

        resultado = validaHorario(horario_inicio, horario_final)

        if resultado is True:
            print("Horario válido")
        else:
            print("Erro:", resultado)

    frame_img.pack_forget()
    frame_login.pack_forget()

    frame_adm_agenda = ctk.CTkFrame(tela, width=1000, height=600)
    frame_adm_agenda.pack()

    label_cirurgia = ctk.CTkLabel(frame_adm_agenda, bg_color="#000000", width=985, height=585, text="", fg_color="#ffffff", corner_radius=12)
    label_cirurgia.place(x=10, y=10)

    label_tipo_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="TIPO DE CIRURGIA", fg_color="transparent", text_color="#000000", bg_color="#ffffff", font=('Arial',16,'bold'))
    label_tipo_cirurgia.place(x=425, y=160)

    tipos_de_cirurgia = obter_tipos_de_cirurgias()

    tipo_selecionado = ctk.StringVar()
    tipo_cirurgia = ctk.CTkComboBox(frame_adm_agenda, variable=tipo_selecionado, values=tipos_de_cirurgia, 
                                        fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                        dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
    tipo_cirurgia.place(x=350, y=200)

    label_data_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="DATA INICIAL", fg_color="transparent", text_color="#000000", bg_color="#ffffff", font=('Arial',16,'bold'))
    label_data_cirurgia.place(x=360, y=250)


    entry_data_inicio = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000")
    entry_data_inicio.place(x=350, y=275)

    label_horario_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="HORARIO INICIAL", fg_color="transparent", text_color="#000000", bg_color="#ffffff", font=('Arial',16,'bold'))
    label_horario_cirurgia.place(x=510, y=250)

    entry_horario_inicio = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000")
    entry_horario_inicio.place(x=510, y=275)
    entry_horario_inicio.bind("<KeyRelease>", formatar_horario)

    label_medio_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="TEMPO MEDIO", fg_color="transparent", text_color="#000000", bg_color="#ffffff", font=('Arial',16,'bold'))
    label_medio_cirurgia.place(x=355, y=320)

    entry_medio_cirurgia = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000")
    entry_medio_cirurgia.place(x=350, y=350)

    label_hora_final_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="HORA FINAL PREVISTA", fg_color="transparent", text_color="#000000", bg_color="#ffffff", font=('Arial',16,'bold'))
    label_hora_final_cirurgia.place(x=500, y=320)
    
    entry_data_fim = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000")
    entry_data_fim.place(x=510, y=350)
    entry_data_fim.bind("<KeyRelease>", formatar_horario)

    def validar_data():
        data_inicio = entry_data_inicio.get()
        data_fim = entry_data_fim.get()

        resultado = validaDtinicioMenorDtfim(data_inicio, data_fim)

        if resultado is True:
            print("Datas válidas.")
        else:
            print("Erro:", resultado)

    botao_validar = ctk.CTkButton(frame_adm_agenda, text="Validar Data", command=validar_data)
    botao_validar.place(x=500, y=450)

    botao_validar_hora = ctk.CTkButton(frame_adm_agenda, text="validar hora", command=validarhora)
    botao_validar_hora.place(x=320, y=450)

    tipos_salas = obter_salas()

    sala_selecionada = ctk.IntVar()
    sala_cirurgia = ctk.CTkComboBox(frame_adm_agenda, variable=sala_selecionada, values=tipos_salas, 
                                        fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                        dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
    sala_cirurgia.place(x=350, y=400)

    def tela_agenda():
        def voltar_para_tela_anterior():
            frame_agenda.pack_forget()
            tela_administrador()

        frame_adm_agenda.pack_forget()

        frame_agenda = ctk.CTkFrame(tela, width=1000, height=600)
        frame_agenda.pack()

        label = ctk.CTkLabel(frame_agenda, bg_color="#000000", width=985, height=585, text="", fg_color="#ffffff", corner_radius=12)
        label.place(x=10, y=10)

        cirurgiaos = obter_cirurgiao()

        cirurgiao_selecionado = ctk.StringVar()
        cirurgiao_box = ctk.CTkComboBox(frame_agenda, variable=cirurgiao_selecionado, values=cirurgiaos, 
                                        fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                        dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
        cirurgiao_box.place(x=350,y=200)

        anestesista = obter_anestesista()

        anestesista_selecionado = ctk.StringVar()
        anestesista_box = ctk.CTkComboBox(frame_agenda, variable=anestesista_selecionado, values=anestesista, 
                                        fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                        dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
        anestesista_box.place(x=350,y=240)

        instrumentador = obter_instrumentador()

        instrumentador_selecionado = ctk.StringVar()
        instrumentador_box = ctk.CTkComboBox(frame_agenda, variable=instrumentador_selecionado, values=instrumentador, 
                                        fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                        dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
        instrumentador_box.place(x=350,y=280)

        botao_voltar = ctk.CTkButton(frame_agenda, text="Voltar", command=voltar_para_tela_anterior)
        botao_voltar.place(x=500, y=500)

        enfermeiros = buscar_enfermeiros()

        estado_cheeckbox = [ctk.BooleanVar() for _ in range(len(enfermeiros))]

        for i, enfermerio in enumerate(enfermeiros):
            cheekbox = ctk.CTkCheckBox(frame_agenda, text=enfermerio[0], variable=estado_cheeckbox[i])
            cheekbox.place(x=400, y=i * 30 + 400)
        
        def obter_selecionados():
            selecionados = [enfermeiros[i][0] for i, estado in enumerate(estado_cheeckbox) if estado.get()]
            print("Itens selecionados: ", selecionados)
        
        botao_obter_selecionados = ctk.CTkButton(frame_agenda, text="Obter Itens Selecionados", command=obter_selecionados)
        botao_obter_selecionados.place(x=500, y=500)

    botao_proximo = ctk.CTkButton(frame_adm_agenda, text="Proximo", command=tela_agenda, fg_color="#00940A", text_color="#000000")
    botao_proximo.place(x=600, y=500)


def tela_comum():
        frame_img.pack_forget()
        frame_login.pack_forget()

        label_texto_tela_cadastro2 = ctk.CTkLabel(tela, text="LOGIN ACESSO 2@", bg_color="#ffffff", text_color="#000000", font=("Roboto", 22, 'bold'))
        label_texto_tela_cadastro2.place(x=115, y=35)
        pass


def tela_registro():

    def mostrar_senha_reg():
        if show_password_var_reg.get():
            entry_senha_registro.configure(show="")
            entry_csenha.configure(show="")
        else:
            entry_senha_registro.configure(show="*")
            entry_csenha.configure(show="*")

    def voltar_login():
        frame_registro.pack_forget()

        frame_login.pack(side=RIGHT)

    def salvar_user():
        usuario = entry_usuario_registro.get()
        senha = entry_senha_registro.get()
        confirmar_senha = entry_csenha.get()
        nivel_aceeso = selected_option.get()

        if senha != confirmar_senha:
            messagebox.showerror(title="Erro no Registro", message="As senhas não coincidem")
            return

        if nivel_aceeso == "Adm":
            nivel_aceeso = "1"
        elif nivel_aceeso == "Comum":
            nivel_aceeso = "2"
        
        try:
            createPerfilDeAcesso(senha, usuario, nivel_aceeso)
            messagebox.showinfo(title="Estado do Cadastro", message="Usuário Registrado com sucesso")
        except Exception as e:
            messagebox.showerror(title="Erro no Registro", message=str(e))

    frame_login.pack_forget()

    frame_registro = ctk.CTkFrame(tela, width=500, height=600)
    frame_registro.pack(side=RIGHT)

    label_cadastro = ctk.CTkLabel(frame_registro, bg_color="#000000", width=350, height=350, text="", fg_color="#ffffff", corner_radius=12)
    label_cadastro.place(x=100, y=115)

    label_texto_tela_cadastro = ctk.CTkLabel(label_cadastro, text="CADASTRO", bg_color="#ffffff", text_color="#000000", font=("Roboto", 22, 'bold'))
    label_texto_tela_cadastro.place(x=115, y=35)

    entry_usuario_registro = ctk.CTkEntry(label_cadastro, placeholder_text="Nome do Usuario", text_color="#565656", border_width=2, width=250, height=40, font=("Roboto", 12), 
                             border_color="#000000", bg_color="#ffffff", placeholder_text_color="#565656", fg_color="#ffffff", corner_radius=10)
    entry_usuario_registro.place(x=50, y=80)

    entry_senha_registro = ctk.CTkEntry(label_cadastro, placeholder_text="Senha do Usuario", placeholder_text_color="#565656", text_color="#565656", show="*",
                                        border_width=2, width=250, height=40, font=("Roboto", 12), border_color="#000000", bg_color="#ffffff", fg_color="#ffffff", corner_radius=10)
    entry_senha_registro.place(x=50, y=130)

    entry_csenha = ctk.CTkEntry(label_cadastro, placeholder_text="Confirmar senha do Usuario", placeholder_text_color="#565656", text_color="#565656", show="*",
                                border_width=2, width=250, height=40, font=("Roboto", 12), border_color="#000000", bg_color="#ffffff", fg_color="#ffffff", corner_radius=10)
    entry_csenha.place(x=50, y=180)

    opcoes = ["Adm", "Comum"]
    selected_option = ctk.StringVar()

    combo = ctk.CTkComboBox(label_cadastro, variable=selected_option, values=opcoes, fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000", 
                            dropdown_text_color="#000000", dropdown_hover_color="#565656")
    combo.place(x=50, y=225)
    combo.set(opcoes[0])

    show_password_var_reg = ctk.BooleanVar()

    cheekbox_reg = ctk.CTkCheckBox(label_cadastro, text="Monstrar senha", fg_color="#000000", text_color="#000000", variable=show_password_var_reg, onvalue=True, offvalue=False, command=mostrar_senha_reg)
    cheekbox_reg.place(x=50, y=260)

    botao_voltar = ctk.CTkButton(label_cadastro, text="VOLTAR", text_color="#ffffff", fg_color="#000000", corner_radius=15, font=("Roboto", 14, 'bold'), 
                               hover_color="#454545", command=voltar_login)
    botao_voltar.place(x=25, y=300)

    botao_registrar = ctk.CTkButton(label_cadastro, text="CADASTRE-SE", text_color="#ffffff", fg_color="#000000", corner_radius=15, font=("Roboto", 14, 'bold'), 
                               hover_color="#454545", command=salvar_user)
    botao_registrar.place(x=175, y=300)

# Cração da tela 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

tela = ctk.CTk()
tela.geometry("1000x600")
tela.title("Cadastro de Cirurgias")
tela.iconbitmap("Python\Cadastro_Login\Cadastro_Login\icone.ico")
tela.resizable(False, False)

frame_img = ctk.CTkFrame(tela, width=500, height=600)
frame_img.pack(side=LEFT)

frame_login = ctk.CTkFrame(tela, width=500, height=600)
frame_login.pack(side=RIGHT)

img = PhotoImage(file="Python\Cadastro_Login\Cadastro_Login\cirurgia.png")
Label_img = ctk.CTkLabel(frame_img, image=img, text="")
Label_img.place(x=5, y=80)

label_tt = ctk.CTkLabel(frame_img, text="Nome do App", font=("Roboto", 20, 'bold'), text_color="#205d5e")
label_tt.place(x=200, y=50)

label_login = ctk.CTkLabel(frame_login, bg_color="#000000", width=350, height=350, text="", fg_color="#ffffff", corner_radius=12)
label_login.place(x=100, y=115)

label_texto = ctk.CTkLabel(label_login, text="BEM VINDO", bg_color="#ffffff", text_color="#000000", font=("Roboto", 22, 'bold'))
label_texto.place(x=115, y=45)

entry_usuario = ctk.CTkEntry(label_login, placeholder_text="Nome do Usuario", text_color="#565656", border_width=2, width=250, height=40, font=("Roboto", 12), 
                             border_color="#000000", bg_color="#ffffff", placeholder_text_color="#565656", fg_color="#ffffff", corner_radius=10)
entry_usuario.place(x=50, y=100)

entry_senha = ctk.CTkEntry(label_login, placeholder_text="Senha do Usuario", placeholder_text_color="#565656", text_color="#565656", show="*",border_width=2, width=250, height=40, font=("Roboto", 12), 
                             border_color="#000000", bg_color="#ffffff", fg_color="#ffffff", corner_radius=10)
entry_senha.place(x=50, y=150)

show_password_var = ctk.BooleanVar()

cheekbox = ctk.CTkCheckBox(label_login, text="Monstrar senha", fg_color="#000000", text_color="#000000", command=mostrar_senha, variable=show_password_var, onvalue=True, offvalue=False)
cheekbox.place(x=50, y=200)

botao_login = ctk.CTkButton(label_login, text="LOGIN", text_color="#ffffff", fg_color="#000000", corner_radius=15, font=("Roboto", 14, 'bold'), hover_color="#454545", command=login)
botao_login.place(x=105, y=225)

label_texto_cadastro = ctk.CTkLabel(label_login, text="AINDA NÃO POSSUI CONTA?", text_color="#000000", font=("Roboto", 14, 'bold'))
label_texto_cadastro.place(x=81, y=260)

botao_registro = ctk.CTkButton(label_login, text="CADASTRE-SE", text_color="#ffffff", fg_color="#000000", corner_radius=15, font=("Roboto", 14, 'bold'), 
                               hover_color="#454545", command=tela_registro)
botao_registro.place(x=105, y=295)

tela.mainloop()
