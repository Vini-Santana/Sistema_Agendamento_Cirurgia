import customtkinter as ctk
import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta, time
from crud import obter_tipos_de_cirurgias, obter_salas, obter_cirurgiao, obter_anestesista, obter_instrumentador, buscar_enfermeiros, obter_tempo_medio, obter_IDs_TodasCirurgias, read, createCirurgia, obter_cirurgias_do_bd, createPaciente, validar_data_nascimento, cliente_existente
from validacoes import validaUsuarioSenha_RetornaNivelAcesso
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

enfermeiros_texto = None

# Criação de outras telas e funções
def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    nivel_acesso = validaUsuarioSenha_RetornaNivelAcesso(usuario, senha)

    if nivel_acesso == 1:
        tela_home()
    else:
        messagebox.showerror(title="Erro no login", message="Credenciais inválidas")

def mostrar_senha():
    if show_password_var.get():
        entry_senha.configure(show="")
    else:
        entry_senha.configure(show="*")

def tela_home():

    def retornaGrafico():
        frame_img.pack_forget()
        frame_login.pack_forget()
        #Descobrindo quantas cirurgias possui de cada status
        Agendadas = 0
        Canceladas = 0
        Concluidas = 0
        todosIds = obter_IDs_TodasCirurgias()
        for idCirurgia in todosIds:
            retornoStatus = read("CIRURGIA", "STATUS", idCirurgia)
            match retornoStatus[0][0]:
                case 1:
                    Agendadas += 1
                case 2: 
                    Concluidas +=1
                case 3: 
                    Canceladas +=1
            
        qtdStatus = []
        status = []
        c = []
        
        #Se os status forem diferente de zero, eles aparecerão na tela
        if Agendadas != 0:
            qtdStatus.append(Agendadas)
            status.append('Agendadas')
            c.append('#085CA6')
        if Concluidas != 0:
            qtdStatus.append(Concluidas)
            status.append('Concluídas')
            c.append('#03AD1D')
        if Canceladas != 0:
            qtdStatus.append(Canceladas)
            status.append('Canceladas')
            c.append('#CC8502')
        
        #O gráfico não será apresentado se TODOS os status forem iguais a zero
        if Agendadas or Concluidas or Canceladas != 0:

            largura_pixels = 500
            altura_pixels = 300
            dpi = 80

            largura_polegadas = largura_pixels / dpi
            altura_polegadas = altura_pixels / dpi

            # Estamos criando a representação, área de plotagem
            figura=plt.Figure(figsize=(largura_polegadas, altura_polegadas), dpi=dpi, layout='compressed')
            ax=figura.add_subplot(111)

            #Inserindo a figura na tela
            canva=FigureCanvasTkAgg(figura, label_grafico)
            canva.get_tk_widget().place(x=0, y=50)


            if len(qtdStatus) == 1:
                wedges, texts, autotexts = ax.pie(qtdStatus, autopct=lambda v:f"{sum(qtdStatus)*v/100:.0f}",shadow=False, pctdistance=0, colors= c)
            else:    
                wedges, texts, autotexts = ax.pie(qtdStatus, autopct=lambda v:f"{sum(qtdStatus)*v/100:.0f}",shadow=False, pctdistance=0.5, colors= c)
            ax.legend(wedges, status,
                    title="Status",
                    loc="center left",
                    bbox_to_anchor=(1, 0, 0.5, 1))
            plt.setp(autotexts, size=20)
            
            label_grafico_cabecalho.configure(text="STATUS DAS CIRURGIAS") 

            label_agendadas = ctk.CTkLabel(label_solicitacoes, text=f"{Agendadas} - Agendadas", font=('Arial', 20), anchor="w", fg_color="#064aa4", text_color="#ffffff", corner_radius=12)
            label_agendadas.place(x=10, y=100)

            label_concluidas = ctk.CTkLabel(label_solicitacoes, text=f"{Concluidas} - Concluídas", font=('Arial', 20), anchor="w", fg_color="#00bf24", text_color="#ffffff", corner_radius=12)
            label_concluidas.place(x=10, y=150)

            label_canceladas = ctk.CTkLabel(label_solicitacoes, text=f"{Canceladas} - Canceladas", font=('Arial', 20), anchor="w", fg_color="#ffa800", text_color="#ffffff", corner_radius=12)
            label_canceladas.place(x=10, y=200)

    frame_img.pack_forget()
    frame_login.pack_forget()

    frame_home = ctk.CTkFrame(tela, width=1000, height=600)
    frame_home.place(x=0)

    frame_lateral = ctk.CTkFrame(tela, width=150, height=600)
    frame_lateral.place(x=0)

    label_home = ctk.CTkLabel(frame_lateral, width=150, height=600, fg_color="#0cc0df", text="")
    label_home.place(x=0)

    img_home = PhotoImage(file="Python\Cadastro_Login\cirurgia.png")
    img_reduzida = img_home.subsample(4,4)
    label_img_home = ctk.CTkLabel(label_home, image=img_reduzida, text="")
    label_img_home.place(x=10)

    def tela_paciente():
        def voltar_para_tela_anterior():
            frame_paciente.pack_forget()
            tela_home()

        def validar_paciente():
            nome = entry_nome.get()
            cpf = entry_cpf.get()
            data_nasc = entry_data.get()

            if not cliente_existente(cpf):
                # Paciente não existe, cadastrar
                createPaciente(nome, data_nasc, cpf)
                messagebox.showinfo(title="Informação", message="Cadastrando Paciente")
            
            tela_administrador()

        frame_paciente = ctk.CTkFrame(tela, width=1000, height=600)
        frame_paciente.pack()

        label_visualizador = ctk.CTkLabel(frame_paciente, bg_color="#000000", width=985, height=585, text="", fg_color="#d9d9d9", corner_radius=12)
        label_visualizador.place(x=10, y=10)

        label_nome = ctk.CTkLabel(frame_paciente, text="NOME DO PACIENTE *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
        label_nome.place(x=425, y=120)

        entry_nome = ctk.CTkEntry(frame_paciente, fg_color="#ffffff", text_color="#000000", width=300, height=30)
        entry_nome.place(x=350, y=150)

        label_cpf = ctk.CTkLabel(frame_paciente, text="CPF DO PACIENTE *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
        label_cpf.place(x=425, y=190)

        def formatar_cpf(event):
            entry_cpf = event.widget
            s = entry_cpf.get()

            cpf = ''.join(filter(str.isdigit, s))

            if len(cpf) == 3 or len(cpf) == 6:
                entry_cpf.insert(ctk.END, '.')

            if len(cpf) == 9:
                entry_cpf.insert(ctk.END, '-')

            if len(cpf) == 12:
                entry_cpf.delete(13, ctk.END)

        entry_cpf = ctk.CTkEntry(frame_paciente, fg_color="#ffffff", text_color="#000000", width=300, height=30)
        entry_cpf.place(x=350, y=220)
        entry_cpf.bind("<KeyRelease>", formatar_cpf)

        label_data = ctk.CTkLabel(frame_paciente, text="DATA DE NASCIMENTO DO PACIENTE *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
        label_data.place(x=350, y=260)

        def formatar_data(event):
            entry_data = event.widget
            s = entry_data.get()

            if len(s) == 2 and s.count('/') == 0:
                entry_data.insert(ctk.END, '/')
            if len(s) == 5 and s.count('/') == 1:
                    entry_data.insert(ctk.END, '/')

            if not validar_data_nascimento(s):
                entry_data.delete(10, ctk.END)

        entry_data = ctk.CTkEntry(frame_paciente, fg_color="#ffffff", text_color="#000000", width=300, height=30)
        entry_data.place(x=350, y=290)
        entry_data.bind("<KeyRelease>", formatar_data)

        botao_voltar_home = ctk.CTkButton(frame_paciente, text="Home", command=voltar_para_tela_anterior, fg_color="#FFD700", text_color="#000000", corner_radius=12, bg_color="#d9d9d9", hover_color="#F0E68C")
        botao_voltar_home.place(x=200, y=460)      

        botao_proximo = ctk.CTkButton(frame_paciente, text="Proximo", command=validar_paciente, fg_color="#00940A", text_color="#000000", corner_radius=12, bg_color="#d9d9d9")
        botao_proximo.place(x=600, y=460)

        def tela_administrador():
            def voltar_para_tela_anterior():
                    frame_adm_agenda.pack_forget()
                    tela_paciente()

            frame_paciente.pack_forget()

            frame_adm_agenda = ctk.CTkFrame(tela, width=1000, height=600)
            frame_adm_agenda.pack()

            label_cirurgia = ctk.CTkLabel(frame_adm_agenda, bg_color="#000000", width=985, height=585, text="", fg_color="#d9d9d9", corner_radius=12)
            label_cirurgia.place(x=10, y=10)

            label_tipo_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="TIPO DE CIRURGIA *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
            label_tipo_cirurgia.place(x=425, y=120)

            tipos_de_cirurgia = obter_tipos_de_cirurgias()

            tipo_selecionado = ctk.StringVar()
            tipo_cirurgia = ctk.CTkComboBox(frame_adm_agenda, variable=tipo_selecionado, values=tipos_de_cirurgia, 
                                                fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                                dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
            tipo_cirurgia.place(x=350, y=150)

            label_data_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="DATA INICIAL *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
            label_data_cirurgia.place(x=360, y=200)


            def formatar_data(event):
                entry_data_inicio = event.widget
                s = entry_data_inicio.get()

                if len(s) == 2 and s.count('/') == 0:
                    entry_data_inicio.insert(ctk.END, '/')
                if len(s) == 5 and s.count('/') == 1:
                        entry_data_inicio.insert(ctk.END, '/')

            entry_data_inicio = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000")
            entry_data_inicio.place(x=350, y=225)
            entry_data_inicio.bind("<KeyRelease>", formatar_data)

            label_data_fim_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="DATA FINAL", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
            label_data_fim_cirurgia.place(x=360, y=320)

            entry_data_fim = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000", state="readonly")
            entry_data_fim.place(x=350, y=350)

            label_horario_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="HORARIO INICIAL *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
            label_horario_cirurgia.place(x=510, y=200)

            def formatar_horario(event):
                entry_data_inicio = event.widget
                s = entry_data_inicio.get()

                if len(s) == 2 and s.count(':') == 0:
                    entry_data_inicio.insert(ctk.END, ':')

                if len(s) > 5:
                    entry_data_inicio.delete(5, ctk.END)

            entry_horario_inicio = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000")
            entry_horario_inicio.place(x=510, y=225)
            entry_horario_inicio.bind("<KeyRelease>", formatar_horario)

            label_medio_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="TEMPO MEDIO", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
            label_medio_cirurgia.place(x=510, y=260)

            entry_medio_cirurgia = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000", state="readonly")
            entry_medio_cirurgia.place(x=510, y=285)

            label_hora_final_cirurgia = ctk.CTkLabel(frame_adm_agenda, text="HORA FINAL PREVISTA", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
            label_hora_final_cirurgia.place(x=500, y=320)

            entry_hora_fim = ctk.CTkEntry(frame_adm_agenda, fg_color="#ffffff", text_color="#000000", state="readonly")
            entry_hora_fim.place(x=510, y=350)

            label_sala = ctk.CTkLabel(frame_adm_agenda, text="SALA *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
            label_sala.place(x=465, y=390)

            tipos_salas = obter_salas()

            tipos_salas.insert(0, "")

            sala_selecionada = ctk.StringVar()  # Use StringVar para armazenar uma string
            sala_cirurgia = ctk.CTkComboBox(frame_adm_agenda, variable=sala_selecionada, values=tipos_salas, 
                                            fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                            dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
            sala_cirurgia.place(x=350, y=415)

            def validar_data_e_hora(data_str, horario_str):
                
                try:
                    data_cirurgia = datetime.strptime(data_str + ' ' + horario_str, '%d/%m/%Y %H:%M')
                    data_atual = datetime.now()

                    if data_cirurgia <= data_atual:
                        return "A data/horário da cirurgia não pode ser no passado."

                    return None
                except ValueError:
                    return "A data ou horário são inválidos. Use o formato DD/MM/AAAA HH:MM."

            def validarhora():
                data_inicio = entry_data_inicio.get()
                horario_inicio = entry_horario_inicio.get()
                erro = validar_data_e_hora(data_inicio, horario_inicio)

                if erro:
                    messagebox.showerror("Data/Horário Incorretos", erro)
                    return

                tempo_medio = obter_tempo_medio(tipo_selecionado.get())

                if tempo_medio is not None:
                    horas_tempo_medio = tempo_medio.seconds // 3600
                    minutos_tempo_medio = (tempo_medio.seconds % 3600) // 60

                    horario_inicio = entry_horario_inicio.get()
                    hora_inicio, minuto_inicio = map(int, horario_inicio.split(':'))

                    # Converter o horário de início em minutos desde a meia-noite
                    minutos_inicio = hora_inicio * 60 + minuto_inicio

                    # Somar o tempo médio em minutos ao horário de início
                    minutos_final = minutos_inicio + (horas_tempo_medio * 60) + minutos_tempo_medio

                    # Calcular as horas e minutos finais
                    hora_final = minutos_final // 60
                    minuto_final = minutos_final % 60

                    # Lidar com o caso em que as horas ultrapassam 24
                    if hora_final >= 24:
                        hora_final -= 24

                    entry_hora_fim.configure(state="normal")
                    entry_hora_fim.delete(0, ctk.END)
                    entry_hora_fim.insert(0, f"{hora_final:02d}:{minuto_final:02d}")
                    entry_hora_fim.configure(state="readonly")

                    data_inicio = entry_data_inicio.get()

                    data_inicio_dt = datetime.strptime(data_inicio, "%d/%m/%Y")

                    # Calcular a data final considerando a ultrapassagem de meia-noite
                    data_hora_inicio = datetime.combine(data_inicio_dt, time(hora_inicio, minuto_inicio))
                    data_hora_final = data_hora_inicio + timedelta(hours=horas_tempo_medio, minutes=minutos_tempo_medio)
                    
                    if data_hora_final.hour >= 24:
                        data_hora_final += timedelta(days=1)

                    data_final = data_hora_final.strftime("%d/%m/%Y")
                    entry_data_fim.configure(state="normal")  # Torna o campo editável
                    entry_data_fim.delete(0, ctk.END)
                    entry_data_fim.insert(0, data_final)
                    entry_data_fim.configure(state="readonly")

                    # Atualize a entrada entry_medio_cirurgia
                    entry_medio_cirurgia.configure(state="normal")  # Torna o campo editável
                    entry_medio_cirurgia.delete(0, ctk.END)
                    entry_medio_cirurgia.insert(0, f"{horas_tempo_medio:02d}:{minutos_tempo_medio:02d}")
                    entry_medio_cirurgia.configure(state="readonly")  # Bloqueia o campo novamente

                else:
                    print("Erro: Tempo médio não encontrado.")

            botao_validar_hora = ctk.CTkButton(frame_adm_agenda, text="Confirmar data/hora", command=validarhora, corner_radius=12, bg_color="#d9d9d9")
            botao_validar_hora.place(x=350, y=285)

            def tela_agenda():
                def voltar_para_tela_anterior():
                    frame_agenda.pack_forget()
                    tela_administrador()

                frame_adm_agenda.pack_forget()

                frame_agenda = ctk.CTkFrame(tela, width=1000, height=600)
                frame_agenda.pack()

                label = ctk.CTkLabel(frame_agenda, bg_color="#000000", width=985, height=585, text="", fg_color="#d9d9d9", corner_radius=12)
                label.place(x=10, y=10)

                label_cirurgiao = ctk.CTkLabel(frame_agenda,text="CIRURGIÃO *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
                label_cirurgiao.place(x=450, y=70)

                cirurgiaos = obter_cirurgiao()

                cirurgiao_selecionado = ctk.StringVar()
                cirurgiao_box = ctk.CTkComboBox(frame_agenda, variable=cirurgiao_selecionado, values=cirurgiaos, 
                                                    fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                                    dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
                cirurgiao_box.place(x=350,y=100)

                label_anestesista = ctk.CTkLabel(frame_agenda,text="ANESTESISTA *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
                label_anestesista.place(x=440, y=135)

                anestesista = obter_anestesista()

                anestesista_selecionado = ctk.StringVar()
                anestesista_box = ctk.CTkComboBox(frame_agenda, variable=anestesista_selecionado, values=anestesista, 
                                                    fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                                    dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
                anestesista_box.place(x=350,y=165)

                label_instrumentador = ctk.CTkLabel(frame_agenda,text="INSTRUMENTADOR *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
                label_instrumentador.place(x=420, y=200)
                instrumentador = obter_instrumentador()

                instrumentador_selecionado = ctk.StringVar()
                instrumentador_box = ctk.CTkComboBox(frame_agenda, variable=instrumentador_selecionado, values=instrumentador, 
                                                    fg_color="#ffffff", dropdown_fg_color="#ffffff", text_color="#000000",
                                                    dropdown_text_color="#000000", dropdown_hover_color="#DCDCDC", width=300)
                instrumentador_box.place(x=350,y=230)

                label_enfermeiros = ctk.CTkLabel(frame_agenda,text="ENFERMEIROS *", fg_color="#d9d9d9", text_color="#000000", bg_color="#d9d9d9", font=('Arial',16,'bold'))
                label_enfermeiros.place(x=430, y=263)

                frame_scrollable = ctk.CTkScrollableFrame(frame_agenda, width=300, fg_color="#DCDCDC", border_width=3, border_color="black")
                frame_scrollable.place(x=340, y=290)

                enfermeiros = buscar_enfermeiros()

                estado_checkbox = [ctk.BooleanVar() for _ in range(len(enfermeiros))]

                for i, enfermeiro in enumerate(enfermeiros):
                    checkbox = ctk.CTkCheckBox(frame_scrollable, text=enfermeiro[0], variable=estado_checkbox[i], text_color="#000000", border_color="#000000")
                    checkbox.pack(fill="x", padx=10, pady=5)

                def obter_selecionados():
                    selecionados = [enfermeiros[i][0] for i, estado in enumerate(estado_checkbox) if estado.get()]
                    print("Itens selecionados: ", selecionados)
        

                botao_obter_selecionados = ctk.CTkButton(frame_agenda, text="Adicionar", command=obter_selecionados, corner_radius=12, width=20, height=20, bg_color="#d9d9d9")
                botao_obter_selecionados.place(x=600, y=265)

                botao_voltar = ctk.CTkButton(frame_agenda, text="Voltar", command=voltar_para_tela_anterior, corner_radius=12, bg_color="#d9d9d9")
                botao_voltar.place(x=300, y=520)

                def obter_selecionados_final():
                    global enfermeiros_texto
                    selecionados = [enfermeiros[i][0] for i, estado in enumerate(estado_checkbox) if estado.get()]
                    enfermeiros_texto.configure(text=f"Enfermeiros - {', '.join(selecionados)}")

                def validar_campo_tela():
                    if (not cirurgiao_selecionado.get() or not anestesista_selecionado.get() or not instrumentador_selecionado.get()):
                        messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
                    elif not any(estado.get() for estado in estado_checkbox):
                        messagebox.showerror("Erro", "Selecione pelo menos um enfermeiro.")
                    else:
                        tela_final()

                def tela_final():
                    frame_agenda.pack_forget()

                    frame_final = ctk.CTkFrame(tela, width=1000, height=600)
                    frame_final.pack()

                    label_final = ctk.CTkLabel(frame_final, bg_color="#d9d9d9", width=985, height=585, text="", fg_color="#d9d9d9", corner_radius=12)
                    label_final.place(x=10, y=10)

                    label_visualização = ctk.CTkLabel(label_final,  bg_color="#ffffff", width=600, height=400, text="", fg_color="#000000", corner_radius=12)
                    label_visualização.place(x=190, y=50)

                    texto_label = ctk.CTkLabel(label_visualização, text="AGENDA", fg_color="transparent", text_color="#ffffff", bg_color="#000000", font=('Arial',24,'bold'))
                    texto_label.place(x=250, y=20)

                    cirurgia_texto = ctk.CTkLabel(label_visualização, text=f"Tipo - {tipo_selecionado.get()}", fg_color="transparent", text_color="#ffffff", bg_color="#000000", font=('Arial',16,'bold'))
                    cirurgia_texto.place(x=20, y=100)

                    cirurgiao_texto = ctk.CTkLabel(label_visualização, text=f"Cirurgião - {cirurgiao_selecionado.get()}", fg_color="transparent", text_color="#ffffff", bg_color="#000000", font=('Arial',16,'bold'))
                    cirurgiao_texto.place(x=20, y=130)

                    anestesista_texto = ctk.CTkLabel(label_visualização, text=f"Anestesista - {anestesista_selecionado.get()}", fg_color="transparent", text_color="#ffffff", bg_color="#000000", font=('Arial',16,'bold'))
                    anestesista_texto.place(x=20, y=160)

                    instrumentador_texto = ctk.CTkLabel(label_visualização, text=f"Instrumentista - {instrumentador_selecionado.get()}", fg_color="transparent", text_color="#ffffff", bg_color="#000000", font=('Arial',16,'bold'))
                    instrumentador_texto.place(x=20, y=190)

                    global enfermeiros_texto
                    enfermeiros_texto = ctk.CTkLabel(label_visualização, text="Enfermeiros -", fg_color="transparent", text_color="#ffffff", bg_color="#000000", font=('Arial',16,'bold'))
                    enfermeiros_texto.place(x=20, y=220)

                    data_texto = ctk.CTkLabel(label_visualização, text=f"Data - {entry_data_inicio.get()} Horario - {entry_horario_inicio.get()}", fg_color="transparent", text_color="#ffffff", bg_color="#000000", font=('Arial',16,'bold'))
                    data_texto.place(x=20, y=250)

                    sala_texto = ctk.CTkLabel(label_visualização, text=f"Sala - {sala_selecionada.get()}", fg_color="transparent", text_color="#ffffff", bg_color="#000000", font=('Arial',16,'bold'))
                    sala_texto.place(x=20, y=290)

                    def cancelado():
                        frame_final.pack_forget()
                        tela_home()

                    botao_cancelar = ctk.CTkButton(label_final, text="Cancelar", fg_color="#F00000", text_color="#ffffff", width=80, hover_color="#FF0000", command=cancelado)
                    botao_cancelar.place(x=190, y=460)

                    def alterar():
                        frame_final.pack_forget()
                        tela_administrador()

                    botao_alterar = ctk.CTkButton(label_final, text="Alterar", text_color="#ffffff", width=80, hover_color="#00FFFF", command=alterar)
                    botao_alterar.place(x=450, y=460)

                    def concluir():
                        dtInicio = entry_data_inicio.get()
                        dtFim = entry_data_fim.get()
                        status = 1
                        nome_paciente = entry_nome.get()
                        cpf_paciente = entry_cpf.get()
                        data_nasc = entry_data.get()
                        hora = entry_horario_inicio.get()
                        fkCirurgiao = cirurgiao_selecionado.get()
                        fkAnestesista = anestesista_selecionado.get()
                        fkInstrumentador = instrumentador_selecionado.get()
                        fkSala = sala_selecionada.get()
                        fkTipo = tipo_selecionado.get()

                        createCirurgia(dtInicio, dtFim, status, nome_paciente, cpf_paciente, data_nasc, hora, fkCirurgiao, fkSala, fkTipo, fkInstrumentador, fkAnestesista)

                        tela_home()

                    botao_concluir = ctk.CTkButton(label_final, text="Concluir", fg_color="#2E8B57",text_color="#ffffff", width=80, hover_color="#00FF00", command=concluir)
                    botao_concluir.place(x=700, y=460)

                    obter_selecionados_final()
                    
                botao_proximo_final = ctk.CTkButton(frame_agenda, text="Proximo", corner_radius=12, command=validar_campo_tela, fg_color="#00940A", text_color="#000000", bg_color="#d9d9d9")
                botao_proximo_final.place(x=630, y=520)

            def validar_campos():
                if (not tipo_selecionado.get() or not entry_data_inicio.get() or not entry_data_fim.get() or 
                    not entry_horario_inicio.get() or not entry_medio_cirurgia.get() or not entry_hora_fim.get()):
                    messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
                elif sala_selecionada.get() == 0:
                    messagebox.showerror("Erro na Sala", "Por favor, escolha uma sala no menu suspenso.")
                else:
                    tela_agenda()
                    
            botao_proximo = ctk.CTkButton(frame_adm_agenda, text="Proximo", command=validar_campos, fg_color="#00940A", text_color="#000000", corner_radius=12, bg_color="#d9d9d9")
            botao_proximo.place(x=600, y=460)

            botao_voltar_paciente = ctk.CTkButton(frame_adm_agenda, text="Voltar", command=voltar_para_tela_anterior, fg_color="#F00000", text_color="#000000", corner_radius=12, bg_color="#d9d9d9", hover_color="#FF6347")
            botao_voltar_paciente.place(x=200, y=460)

    botao_nova_agenda = ctk.CTkButton(frame_lateral, width=130, height=50, fg_color="#252525", text="Nova Agenda", font=('Arial',16,'bold'), command=tela_paciente)
    botao_nova_agenda.place(x=10, y=200)

    def agendas():
        frame_home.pack_forget()

        frame_agendas = ctk.CTkFrame(tela, width=1000, height=600)
        frame_agendas.place(x=0)

        frame_menu_lateral = ctk.CTkFrame(tela, width=150, height=600)
        frame_menu_lateral.place(x=0)

        label_agenda = ctk.CTkLabel(frame_menu_lateral, width=150, height=600, fg_color="#0cc0df", text="")
        label_agenda.place(x=0)

        img_home = PhotoImage(file="Python\Cadastro_Login\cirurgia.png")
        img_reduzida = img_home.subsample(4,4)
        label_img_home = ctk.CTkLabel(label_agenda, image=img_reduzida, text="")
        label_img_home.place(x=10)

        label_visu_agendas = ctk.CTkLabel(frame_agendas, width=850, height=600, fg_color="#d9d9d9", text="")
        label_visu_agendas.place(x=150)

        label_opcoes_agenda = ctk.CTkLabel(label_visu_agendas, width=810, height=100, fg_color="#bbbbbb", text="")
        label_opcoes_agenda.place(x=20,y=10)

        def voltar_home():
            for widget in label_visu_agendas.winfo_children():  
                widget.destroy()
            frame_agendas.pack_forget()
            frame_menu_lateral.pack_forget()

            tela_home()

        botao_nova_agenda = ctk.CTkButton(frame_menu_lateral, width=130, height=50, fg_color="#252525", text="Home", font=('Arial',16,'bold'), command=voltar_home)
        botao_nova_agenda.place(x=10, y=170)

        botao_nova_agenda = ctk.CTkButton(frame_menu_lateral, width=130, height=50, fg_color="#252525", text="Nova Agenda", font=('Arial',16,'bold'), command=tela_paciente)
        botao_nova_agenda.place(x=10, y=230)

        def exibir_cirurgias():
            cirurgias = obter_cirurgias_do_bd()

            y_pos = 120
            for cirurgia in cirurgias:
                if cirurgia[4] == 1:
                    status_descricao = "Agendado"
                elif cirurgia[4] == 2:
                    status_descricao = "Concluído"
                elif cirurgia[4] == 3:
                    status_descricao = "Cancelado"
                else:
                    status_descricao = "Desconhecido"

                texto_label = f"TIPO - {cirurgia[0]} STATUS: {status_descricao}\n Cirurgião - {cirurgia[2]}\n DATA - {cirurgia[2]}, HORARIO - {cirurgia[3]}"

                label_cirurgia = ctk.CTkLabel(label_visu_agendas, text=texto_label, width=810, height=100, fg_color="#8aceff", text_color="#000000")
                label_cirurgia.place(x=20, y=y_pos)

                y_pos += 120

        def info():
            messagebox.showinfo(title="Sistema de Cirurgias", message="Você já esta na tela de agendas")

        botao_agenda = ctk.CTkButton(frame_menu_lateral, width=130, height=50, fg_color="#252525", text="Agendas", font=('Arial',16,'bold'), command=info)
        botao_agenda.place(x=10, y=290)

        botao_atualizar = ctk.CTkButton(frame_menu_lateral, text="Atualizar", width=130, height=50, fg_color="#252525", font=('Arial',16,'bold'), command=exibir_cirurgias)
        botao_atualizar.place(x=10, y=350)
        
        exibir_cirurgias()

    botao_agenda = ctk.CTkButton(frame_lateral, width=130, height=50, fg_color="#252525", text="Agendas", font=('Arial',16,'bold'), command=agendas)
    botao_agenda.place(x=10, y=300)

    label_visu_home = ctk.CTkLabel(frame_home, width=850, height=600, fg_color="#d9d9d9", text="")
    label_visu_home.place(x=150)

    texto_home = ctk.CTkLabel(label_visu_home, text="HOME", text_color="#000000", font=('Arial',34,'bold'))
    texto_home.place(x=20,y=50)

    label_solicitacoes = ctk.CTkLabel(label_visu_home, width=300, height=350, fg_color="#ede9e9", text="")
    label_solicitacoes.place(x=20, y=120)

    label_solicitacoes_cabecalho = ctk.CTkLabel(label_solicitacoes, width=300, height=55, fg_color="#bbbbbb", text="MINHAS SOLICITAÇÔES", text_color="#000000", font=('Arial', 18, 'bold'))
    label_solicitacoes_cabecalho.place(x=0,y=0)

    label_grafico = ctk.CTkLabel(label_visu_home, width=480, height=350, fg_color="#ede9e9", text="")
    label_grafico.place(x=340, y=120)

    label_grafico_cabecalho = ctk.CTkLabel(label_grafico, width=480, height=55, fg_color="#bbbbbb", text="MINHAS SOLICITAÇÔES", text_color="#000000", font=('Arial', 18, 'bold'))
    label_grafico_cabecalho.place(x=0,y=0)

    retornaGrafico()

# Cração da tela 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

tela = ctk.CTk()
tela.geometry("1000x600")
tela.title("Cadastro de Cirurgias")
tela.iconbitmap("Python\Cadastro_Login\icone.ico")
tela.resizable(False, False)

frame_img = ctk.CTkFrame(tela, width=500, height=600)
frame_img.pack(side=LEFT)

frame_login = ctk.CTkFrame(tela, width=500, height=600)
frame_login.pack(side=RIGHT)

img = PhotoImage(file="Python\Cadastro_Login\cirurgia.png")
Label_img = ctk.CTkLabel(frame_img, image=img, text="")
Label_img.place(x=5, y=80)

label_tt = ctk.CTkLabel(frame_img, text="Sistema Gerenciador de Cirurgias", font=("Roboto", 20, 'bold'), text_color="#205d5e")
label_tt.place(x=100, y=50)

label_login = ctk.CTkLabel(frame_login, bg_color="#000000", width=350, height=350, text="", fg_color="#ffffff", corner_radius=12)
label_login.place(x=100, y=115)

label_texto = ctk.CTkLabel(label_login, text="Bem-Vindo", bg_color="#ffffff", text_color="#000000", font=("Roboto", 22, 'bold'))
label_texto.place(x=115, y=45)

entry_usuario = ctk.CTkEntry(label_login, placeholder_text="Digite seu usuário", text_color="#565656", border_width=2, width=250, height=40, font=("Roboto", 12), 
                             border_color="#000000", bg_color="#ffffff", placeholder_text_color="#565656", fg_color="#ffffff", corner_radius=10)
entry_usuario.place(x=50, y=100)

entry_senha = ctk.CTkEntry(label_login, placeholder_text="Digite sua senha", placeholder_text_color="#565656", text_color="#565656", show="*",border_width=2, width=250, height=40, font=("Roboto", 12), 
                             border_color="#000000", bg_color="#ffffff", fg_color="#ffffff", corner_radius=10)
entry_senha.place(x=50, y=150)

show_password_var = ctk.BooleanVar()

cheekbox = ctk.CTkCheckBox(label_login, text="Monstrar senha", fg_color="#000000", text_color="#000000", command=mostrar_senha, variable=show_password_var, onvalue=True, offvalue=False)
cheekbox.place(x=50, y=210)

botao_login = ctk.CTkButton(label_login, text="Entrar", text_color="#ffffff", fg_color="#000000", corner_radius=15, font=("Roboto", 14, 'bold'), hover_color="#454545", command=login)
botao_login.place(x=105, y=250)

tela.mainloop()
