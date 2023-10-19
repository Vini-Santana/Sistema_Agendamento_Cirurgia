import conexao
##EXEMPLOS DE INSERÇÃO

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
    
def createEquipamentos(equip):
    comando = f'INSERT INTO EQUIPAMENTOS(NOME) VALUES ("{equip}")'
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
    
def createTipo_Cirurgia(tpCirurgia, fkEspecializacao):
    comando = f'INSERT INTO TIPO_CIRURGIA(TIPOCIRURGIA,FKESPECIALIZACAO) VALUES ("{tpCirurgia}",{fkEspecializacao})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createEspecializacao_Cirurgiao(fkCirurgiao, fkEspecializacao):
    comando = f'INSERT INTO TIPO_CIRURGIA(TIPOCIRURGIA,FKESPECIALIZACAO) VALUES ({fkCirurgiao},{fkEspecializacao})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createRecepcionista(dtnascimento, nome, email, fkPrfil):
    comando = f'INSERT INTO RECEPCIONISTA(DTNASCIMENTO,NOME,EMAIL,FKPERFILACESSO) VALUES ("{dtnascimento}","{nome}","{email}", {fkPrfil})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

def createSala_Equipamentos(fkSala, fkEquipamento):
    comando = f'INSERT INTO SALA_EQUIPAMENTOS(FKSALA,FKEQUIPAMENTO) VALUES ({fkSala},{fkEquipamento})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createPaciente(nome, dtnascimento, endereco, numCarteira, email, fkRecepcionista):
    comando = f'INSERT INTO PACIENTE(NOME,DTNASCIMENTO,ENDERECO,NUMCARTEIRA,EMAIL,FKRECEPCIONISTA) VALUES ("{nome}","{dtnascimento}","{endereco}","{numCarteira}","{email}", {fkRecepcionista})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def createCirurgia(dtInicio, dtFim, fkCirurgiao, fkRecepcionista, fkSala, fkTipo, fkPaciente, fkInstrumentador, fkAnestesista):
    
    comando = f'INSERT INTO CIRURGIA(DTINICIO,DTFIM,FKCIRURGIAO,FKRECEPCIONISTA,FKSALA,FKTIPO,FKPACIENTE,FKINSTRUMENTADOR,FKANESTESISTA) VALUES ("{dtInicio}","{dtFim}",{fkCirurgiao},{fkRecepcionista},{fkSala},{fkTipo},{fkPaciente},{fkInstrumentador},{fkAnestesista})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

def createCirurgia_Enfermeiro(fkCirurgia, fkEnfermeiro):
    comando = f'INSERT INTO CIRURGIA_ENFERMEIRO(FKCIRURGIA,FKENFERMEIRO) VALUES ({fkCirurgia},{fkEnfermeiro})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
def createTelefone(ddd, telefone, nomeDaTabela, fkRegistro):
    match nomeDaTabela:
        case 1:
            nomeDaTabela = 'FKENFERMEIRO'
        case 2:
            nomeDaTabela = "FKCIRURGIAO"
        case 3:
            nomeDaTabela = 'FKPACIENTE'
        case 4:
            nomeDaTabela = "FKINSTRUMENTADOR"
        case 5:
            nomeDaTabela = "FKANESTESISTA"
        case 6:
            nomeDaTabela = "FKRECEPCIONISTA"
        case _:
            print("Erro")####
    comando = f'INSERT INTO TELEFONE(DDD,TELEFONE,{nomeDaTabela}) VALUES ({ddd},"{telefone}",{fkRegistro})'
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


#READ#
def read(nomeDaTabela, atributo, id):
    consulta = f'SELECT {atributo} FROM {nomeDaTabela} WHERE ID{nomeDaTabela} = {id}'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()
    return resultadoFim
print(read("cirurgia", "fkCirurgiao, fkAnestesista", 2))
    
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
   