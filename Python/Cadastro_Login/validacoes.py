import conexao
from datetime import datetime
from tkinter import messagebox

#Método valida se usuário e senha estão corretos. Se sim retorna True, se não retorna ValueError
def validaUsuarioSenha_RetornaNivelAcesso(usuario, senha):
     
    consulta = f'SELECT SENHA FROM PERFILDEACESSO WHERE USUARIO = "{usuario}"'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()    
    if resultadoFim == [] or senha != resultadoFim[0][0]:
        print("Usuário ou senha incorretos")
    else:
        return True
    
#VALIDA SE A DATA DE INÍCIO DA CIRURGIA É MENOR QUE DATA FIM
def validaDtinicioMenorDtfim(data_inicio, data_fim):
    try:
        data_inicio_dt = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_fim_dt = datetime.strptime(data_fim, "%d/%m/%Y")

        if data_inicio_dt > data_fim_dt:
            raise ValueError("Data de início da cirurgia deve ser menor que a data de término prevista.")
        else:
            return True

    except ValueError as e:
        return str(e)
def validaSalaDisponivel(dtInicio, horaInicio, dtFim, horaFim):
    dtInicio =  datetime.strptime(dtInicio + " " + horaInicio, '%d/%m/%Y %H:%M:%S')
    dtFim = datetime.strptime(dtFim + " " + horaFim, '%d/%m/%Y %H:%M:%S')
    consulta = f'SELECT NUMEROSALA FROM SALA WHERE IDSALA NOT IN (SELECT FKSALA FROM CIRURGIA WHERE ("{dtInicio}" > concat(dtinicio, ' ' horainicio) AND "{dtInicio}" < concat(dtFim, ' ' horaFim)) OR ("{dtFim}" > concat(dtinicio, ' ' horainicio) AND "{dtFim}" < concat(dtFim, ' ' horaFim)) OR ("{dtInicio}" < concat(dtinicio, ' ' horainicio) AND "{dtFim}" > concat(dtFim, ' ' horaFim)))'
    conexao.cursor.execute(consulta)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

def validaNomeCirurgiaoDisponivel(dtInicio, horaInicio, dtFim, horaFim):
    dtInicio =  datetime.strptime(dtInicio + " " + horaInicio, '%d/%m/%Y %H:%M:%S')
    dtFim = datetime.strptime(dtFim + " " + horaFim, '%d/%m/%Y %H:%M:%S')
    consulta = f'SELECT NOME FROM CIRURGIAO WHERE IDCIRURGIAO NOT IN (SELECT FKCIRURGIAO FROM CIRURGIA WHERE ("{dtInicio}" > concat(dtinicio, ' ' horainicio) AND "{dtInicio}" < concat(dtFim, ' ' horaFim)) OR ("{dtFim}" > concat(dtinicio, ' ' horainicio) AND "{dtFim}" < concat(dtFim, ' ' horaFim)) OR ("{dtInicio}" < concat(dtinicio, ' ' horainicio) AND "{dtFim}" > concat(dtFim, ' ' horaFim)))'
    conexao.cursor.execute(consulta)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

def validaNomeInstrumentadorDisponivel(dtInicio, horaInicio, dtFim, horaFim):
    dtInicio =  datetime.strptime(dtInicio + " " + horaInicio, '%d/%m/%Y %H:%M:%S')
    dtFim = datetime.strptime(dtFim + " " + horaFim, '%d/%m/%Y %H:%M:%S')
    consulta = f'SELECT NOME FROM INSTRUMENTADOR WHERE IDINSTRUMENTADOR NOT IN (SELECT FKINSTRUMENTADOR FROM CIRURGIA WHERE ("{dtInicio}" > concat(dtinicio, ' ' horainicio) AND "{dtInicio}" < concat(dtFim, ' ' horaFim)) OR ("{dtFim}" > concat(dtinicio, ' ' horainicio) AND "{dtFim}" < concat(dtFim, ' ' horaFim)) OR ("{dtInicio}" < concat(dtinicio, ' ' horainicio) AND "{dtFim}" > concat(dtFim, ' ' horaFim)))'
    conexao.cursor.execute(consulta)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

def validaNomeAnestesistaDisponivel(dtInicio, horaInicio, dtFim, horaFim):
    dtInicio =  datetime.strptime(dtInicio + " " + horaInicio, '%d/%m/%Y %H:%M:%S')
    dtFim = datetime.strptime(dtFim + " " + horaFim, '%d/%m/%Y %H:%M:%S')
    consulta = f'SELECT NOME FROM ANESTESISTA WHERE IDANESTESISTA NOT IN (SELECT FKANESTESISTA FROM CIRURGIA WHERE ("{dtInicio}" > concat(dtinicio, ' ' horainicio) AND "{dtInicio}" < concat(dtFim, ' ' horaFim)) OR ("{dtFim}" > concat(dtinicio, ' ' horainicio) AND "{dtFim}" < concat(dtFim, ' ' horaFim)) OR ("{dtInicio}" < concat(dtinicio, ' ' horainicio) AND "{dtFim}" > concat(dtFim, ' ' horaFim)))'
    conexao.cursor.execute(consulta)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

def validaNomeEnfermeiroDisponivel(dtInicio, horaInicio, dtFim, horaFim):
    dtInicio =  datetime.strptime(dtInicio + " " + horaInicio, '%d/%m/%Y %H:%M:%S')
    dtFim = datetime.strptime(dtFim + " " + horaFim, '%d/%m/%Y %H:%M:%S')
    consulta = f'SELECT NOME FROM ENFERMEIRO WHERE IDENFERMEIRO NOT IN (SELECT FKENFERMEIRO FROM CIRURGIA WHERE ("{dtInicio}" > concat(dtinicio, ' ' horainicio) AND "{dtInicio}" < concat(dtFim, ' ' horaFim)) OR ("{dtFim}" > concat(dtinicio, ' ' horainicio) AND "{dtFim}" < concat(dtFim, ' ' horaFim)) OR ("{dtInicio}" < concat(dtinicio, ' ' horainicio) AND "{dtFim}" > concat(dtFim, ' ' horaFim)))'
    conexao.cursor.execute(consulta)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

#VALIDA SE TEM SALA, CIRURGIÃO, ANESTESISTA, INSTRUMENTADOR E ENFERIMEIRO DISPONÍVEIS PARA CIRURGIA
def validaProfissionaisESalaDisponiveis(dtInicio, dtFim):
    consulta = f'SELECT IDSALA FROM SALA WHERE IDSALA NOT IN (SELECT FKSALA FROM CIRURGIA WHERE (("{dtInicio}" > DTINICIO AND "{dtInicio}" < DTFIM) OR ("{dtFim}" > DTINICIO AND "{dtFim}" < DTFIM) OR ("{dtInicio}" < DTINICIO AND "{dtFim}" > DTFIM))'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()
    msg =[]
    if resultadoFim == []:
        msg.append("Nenhuma sala de cirurgia disponível na data inserida")
        
    consulta = f'SELECT IDCIRURGIAO FROM CIRURGIAO WHERE IDCIRURGIAO NOT IN (SELECT FKCIRURGIAO FROM CIRURGIA WHERE ("{dtInicio}" > DTINICIO AND "{dtInicio}" < DTFIM) OR ("{dtFim}" > DTINICIO AND "{dtFim}" < DTFIM) OR ("{dtInicio}" < DTINICIO AND "{dtFim}" > DTFIM))'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()
    if resultadoFim == []:
        msg.append("Nenhum cirurgião disponível na data inserida")
        
    consulta = f'SELECT IDANESTESISTA FROM ANESTESISTA WHERE IDANESTESISTA NOT IN (SELECT FKANESTESISTA FROM CIRURGIA WHERE ("{dtInicio}" > DTINICIO AND "{dtInicio}" < DTFIM) OR ("{dtFim}" > DTINICIO AND "{dtFim}" < DTFIM) OR ("{dtInicio}" < DTINICIO AND "{dtFim}" > DTFIM))'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()
    if resultadoFim == []:
        msg.append("Nenhum anestesista disponível na data inserida")
        
    consulta = f'SELECT IDINSTRUMENTADOR FROM INSTRUMENTADOR WHERE IDINSTRUMENTADOR NOT IN (SELECT FKINSTRUMENTADOR FROM CIRURGIA WHERE ("{dtInicio}" > DTINICIO AND "{dtInicio}" < DTFIM) OR ("{dtFim}" > DTINICIO AND "{dtFim}" < DTFIM) OR ("{dtInicio}" < DTINICIO AND "{dtFim}" > DTFIM))'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()
    if resultadoFim == []:
        msg.append("Nenhum instrumentador disponível na data inserida")
        
    consulta = f'SELECT IDENFERMEIRO FROM ENFERMEIRO WHERE IDENFERMEIRO NOT IN (SELECT AO.FKENFERMEIRO FROM CIRURGIA_ENFERMEIRO AO, CIRURGIA A WHERE ("{dtInicio}" > A.DTINICIO AND "{dtInicio}" < A.DTFIM) OR ("{dtFim}" > A.DTINICIO AND "{dtFim}" < A.DTFIM) OR ("{dtInicio}" < A.DTINICIO AND "{dtFim}" > A.DTFIM))'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall() 
    if resultadoFim == []:
        msg.append("Nenhum enfermeiro disponível na data inserida")
        
    if msg != []:
        raise ValueError(msg)
    else:
        return True
    
print(validaNomeInstrumentadorDisponivel("25/04/2023", "7:05:27", "25/04/2023", "16:05:12"))