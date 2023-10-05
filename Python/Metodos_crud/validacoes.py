import conexao
from datetime import datetime
#Método valida se usuário e senha estão corretos. Se sim retorna True, se não retorna ValueError
def validaUsuarioSenha_RetornaNivelAcesso(usuario, senha):
     
    consulta = f'SELECT SENHA FROM PERFILDEACESSO WHERE USUARIO = "{usuario}"'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()    
    if resultadoFim == [] or senha != resultadoFim[0][0]:
        raise ValueError("Usuário ou senha incorretos")
    else:
        return True

#VALIDAÇÃO DO PARÂMETRO EM OUTRAS CIRURGIAS
#CIRURGIÃO
def validaCirurgiaoEmOutraCirurgia(dtInicio, dtFim):
    consulta = f'SELECT FKCIRURGIAO FROM cirurgia WHERE ("{dtInicio}" > DTINICIO AND "{dtInicio}" < DTFIM) OR ("{dtFim}" > DTINICIO AND "{dtFim}" < DTFIM) OR ("{dtInicio}" < DTINICIO AND "{dtFim}" > DTFIM)'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()
    if resultadoFim == []:
        return resultadoFim
    else:
        raise ReferenceError(f"O Cirurgião não está disponível na data marcada({dtInicio} - {dtFim})")
    #VALIDAR SE A FKRETORNADA ESTÁ EM OUTRA CIRURGIA
    
    
    
#print(validaParametroEntreDtInicioDtfimCom("2023/02/03 04:03:03", "2023/02/03 07:03:03"))

def validaDtinicioMenorDtfim(DtInicio, DtFim):
    
    if datetime.strptime(f"{DtInicio}",  "%Y/%m/%d %H:%M:%S") > datetime.strptime(f"{DtFim}",  "%Y/%m/%d %H:%M:%S"):
        raise ValueError("Data/horário de início da cirurgia deve ser maior que data/horário previsto de término")
    else:
        return True
    
print(validaCirurgiaoEmOutraCirurgia("2023/02/03 06:03:03", "2023/02/03 12:03:03"))



