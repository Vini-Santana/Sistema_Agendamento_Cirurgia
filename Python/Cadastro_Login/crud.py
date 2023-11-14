import conexao
from datetime import datetime
from tkinter import messagebox

def createTesteData(data, data2):
    comando = f'INSERT INTO teste (dtInicio, dtFim) VALUES (str_to_date("{data}", "%Y-%m-%d %k:%i:%s"), str_to_date("{data2}", "%Y-%m-%d %k:%i:%s"))'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
##FIM EXEMPLOS DE INSERÇÃO

##CREATE##
def createEspecializacao(especilizacao):
    comando = f'INSERT INTO ESPECIALIZACAO(ESPECIALIZACAO) VALUES ("{especilizacao}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

def createSala(numSala):
    comando = f'INSERT INTO SALA(NUMEROSALA) VALUES ("{numSala}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createPerfilDeAcesso(senha, usuario, nivel):
    comando = f'INSERT INTO PERFILDEACESSO(SENHA,USUARIO,NIVEL) VALUES ("{senha}","{usuario}",{nivel})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createEnfermeiro(dtnascimento, nome, email):
    comando = f'INSERT INTO ENFERMEIRO(DTNASCIMENTO,NOME,EMAIL) VALUES ("{dtnascimento}","{nome}","{email}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createInstrumentador(dtnascimento, nome, email):
    comando = f'INSERT INTO INSTRUMENTADOR(DTNASCIMENTO,NOME,EMAIL) VALUES ("{dtnascimento}","{nome}","{email}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createAnestesista(dtnascimento, nome, email):
    comando = f'INSERT INTO ANESTESISTA(DTNASCIMENTO,NOME,EMAIL) VALUES ("{dtnascimento}","{nome}","{email}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createCirurgiao(dtnascimento, nome, email):
    comando = f'INSERT INTO CIRURGIAO(DTNASCIMENTO,NOME,EMAIL) VALUES ("{dtnascimento}","{nome}","{email}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createTipo_Cirurgia(tpCirurgia, tempoMedio, fkEspecializacao):
    comando = f'INSERT INTO TIPO_CIRURGIA(TIPOCIRURGIA, TEMPOMEDIO, FKESPECIALIZACAO) VALUES ("{tpCirurgia}", "{tempoMedio}", {fkEspecializacao})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createEspecializacao_Cirurgiao(fkCirurgiao, fkEspecializacao):
    comando = f'INSERT INTO ESPECIALIZACAO_CIRURGIAO(FKCIRURGIAO, FKESPECIALIZACAO) VALUES ({fkCirurgiao},{fkEspecializacao})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createPaciente(nome, dtnascimento, CPF):
    data_nascimento_formatada = datetime.strptime(dtnascimento, '%d/%m/%Y').strftime('%Y-%m-%d')

    comando = f'INSERT INTO PACIENTE(NOME,DTNASCIMENTO,CPF) VALUES ("{nome}","{data_nascimento_formatada}","{CPF}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

#STATUS: 1 - AGENDADA, 2 - CONCLUÍDA 3 - CANCELADA    
def createCirurgia(dtInicio, dtFim, status, horaInicio, horaFim, fkcirurgiao, fkSala, fktipo, fkpaciente, fkinstrumentador, fkanestesista):

    #dtInicio = datetime.strptime(dtInicio, '%d/%m/%Y').strftime('%Y-%m-%d')
    #dtFim = datetime.strptime(dtFim, '%d/%m/%Y').strftime('%Y-%m-%d')

    comando = f'INSERT INTO CIRURGIA(DTINICIO, DTFIM, STATUS, HORAINICIO, HORAFIM, FKCIRURGIAO, FKSALA, FKTIPO, FKPACIENTE, FKINSTRUMENTADOR, FKANESTESISTA) VALUES ("{dtInicio}","{dtFim}","{status}","{horaInicio}","{horaFim}","{fkcirurgiao}","{fkSala}","{fktipo}","{fkpaciente}","{fkinstrumentador}","{fkanestesista}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

def createCirurgia_Enfermeiro(fkCirurgia, fkEnfermeiro):
    comando = f'INSERT INTO CIRURGIA_ENFERMEIRO(FKCIRURGIA,FKENFERMEIRO) VALUES ({fkCirurgia},{fkEnfermeiro})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

#DELETE#

def delete(nomeDaTabela, id):
    comando = f'DELETE FROM {nomeDaTabela} WHERE ID{nomeDaTabela} = {id}'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

#UPDATE#

def update(nomeDaTabela, nomeDaColuna, valor, IdDoRegistro):
    comando = f'UPDATE {nomeDaTabela} SET {nomeDaColuna} = "{valor}" WHERE ID{nomeDaTabela} = {IdDoRegistro}'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

def cancelar(idCirurgia):
    try:
       update_query = f"UPDATE CIRURGIA SET STATUS = 3 WHERE IDCIRURGIA = {idCirurgia}"
       conexao.cursor.execute(update_query)
       conexao.conexaov.commit()
       messagebox.showinfo(title="Info", message="Clique no botão atualizar")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Erro ao cancelar a cirurgia {idCirurgia}: {str(e)}")

def concluir(idCirurgia):
    try:
       update_query = f"UPDATE CIRURGIA SET STATUS = 2 WHERE IDCIRURGIA = {idCirurgia}"
       conexao.cursor.execute(update_query)
       conexao.conexaov.commit()
       messagebox.showinfo(title="Info", message="Clique no botão atualizar")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Erro ao concluir a cirurgia {idCirurgia}: {str(e)}")


#READ#
def read(nomeDaTabela, atributo, id):
    consulta = f'SELECT {atributo} FROM {nomeDaTabela} WHERE ID{nomeDaTabela} = {id}'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()
    return resultadoFim

def obter_id(nome_da_tabela, id_nome_tabela, nome):
    try:
        consulta = f'SELECT {id_nome_tabela} FROM {nome_da_tabela} WHERE NOME = "{nome}"'
        conexao.cursor.execute(consulta)
        resultado = conexao.cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return None
    finally:
        # Adicione essa linha para garantir que os resultados sejam lidos e processados
        conexao.cursor.fetchall()

def obter_id_tipo(nome_da_tabela, id_nome_tabela, nome):
    try:
        consulta = f'SELECT {id_nome_tabela} FROM {nome_da_tabela} WHERE TIPOCIRURGIA = "{nome}"'
        conexao.cursor.execute(consulta)
        resultado = conexao.cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return None
    finally:
        # Adicione essa linha para garantir que os resultados sejam lidos e processados
        conexao.cursor.fetchall()

def obter_id_sala(nome_da_tabela, id_nome_tabela, nome):
    try:
        consulta = f'SELECT {id_nome_tabela} FROM {nome_da_tabela} WHERE NUMEROSALA = "{nome}"'
        conexao.cursor.execute(consulta)
        resultado = conexao.cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return None
    finally:
        # Adicione essa linha para garantir que os resultados sejam lidos e processados
        conexao.cursor.fetchall()

def obter_IDs_TodasCirurgias():
    comando = "SELECT * FROM CIRURGIA"
    conexao.cursor.execute(comando)
    tipos_de_cirurgias = [row[0] for row in conexao.cursor.fetchall()]
    return tipos_de_cirurgias
    
def obter_tipos_de_cirurgias():
    comando = "SELECT TIPOCIRURGIA FROM TIPO_CIRURGIA"
    conexao.cursor.execute(comando)
    tipos_de_cirurgias = [row[0] for row in conexao.cursor.fetchall()]
    return tipos_de_cirurgias

def obter_salas():
    comando = "SELECT NUMEROSALA FROM SALA"
    conexao.cursor.execute(comando)
    tipos_salas = [str(row[0]) for row in conexao.cursor.fetchall()]
    return tipos_salas

def obter_cirurgiao():
    comando = "SELECT NOME FROM CIRURGIAO"
    conexao.cursor.execute(comando)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

def obter_anestesista():
    comando = "SELECT NOME FROM ANESTESISTA"
    conexao.cursor.execute(comando)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

def obter_instrumentador():
    comando = "SELECT NOME FROM INSTRUMENTADOR"
    conexao.cursor.execute(comando)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

def buscar_enfermeiros():
    comando = "SELECT NOME FROM ENFERMEIRO"
    conexao.cursor.execute(comando)
    resultado = conexao.cursor.fetchall()
    return resultado

def obter_tempo_medio(tipo_cirurgia):
    query = "SELECT TEMPOMEDIO FROM TIPO_CIRURGIA WHERE TIPOCIRURGIA = %s"
    conexao.cursor.execute(query, (tipo_cirurgia,))

    resultado = conexao.cursor.fetchone()

    if resultado:
        tempo_medio = resultado[0]
        return tempo_medio
    else:
        return None
    
def obter_cirurgias_do_bd():
    comando = "SELECT FKTIPO, FKCIRURGIAO, DTINICIO, HORA, STATUS, IDCIRURGIA FROM CIRURGIA"
    conexao.cursor.execute(comando)
    cirurgias = conexao.cursor.fetchall()
    return cirurgias

def cliente_existente(cpf):
    comando = f'SELECT COUNT(*) FROM PACIENTE WHERE CPF = "{cpf}"'
    conexao.cursor.execute(comando)
    resultado = conexao.cursor.fetchone()[0]

    return resultado > 0

def validar_data_nascimento(data_nasc):
    try:
        data_nascimento = datetime.strptime(data_nasc, '%d/%m/%Y')
        data_minima = datetime.now().replace(year=datetime.now().year - 110)
        data_maxima = datetime.now().replace(year=datetime.now().year - 18)

        return data_minima <= data_nascimento <= data_maxima
    except ValueError:
        return False
    
def obter_tipo_por_id(id):
    comando = f'SELECT TIPOCIRURGIA FROM TIPO_CIRURGIA WHERE IDTIPO = %s'
    conexao.cursor.execute(comando, (id,))
    resultado = conexao.cursor.fetchone()
    return resultado[0] if resultado else None

def obter_nome_cirurgiao_por_id(id_cirurgiao):
    consulta = 'SELECT NOME FROM CIRURGIAO WHERE IDCIRURGIAO = %s'
    conexao.cursor.execute(consulta, (id_cirurgiao,))
    resultado = conexao.cursor.fetchone()
    return resultado[0] if resultado else None