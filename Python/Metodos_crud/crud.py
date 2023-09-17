import conexao
import datetime
##EXEMPLOS DE INSERÇÃO
def create(nome_produto, valor):
    comando = f'INSERT INTO vendas (nome_produto, valor)VALUES ("{nome_produto}", {valor})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

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
    comando = f'INSERT INTO Sala(NUMEROSALA) VALUES ("{numSala}")'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    
def validaParametroEntreDtInicioDtfimCom(dtInicio, dtFim):
    consulta = f'SELECT * FROM TESTE WHERE ("{dtInicio}" > DTINICIO AND "{dtInicio}" < DTFIM) OR ("{dtFim}" > DTINICIO AND "{dtFim}" < DTFIM) OR ("{dtInicio}" < DTINICIO AND "{dtFim}" > DTFIM)'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()
    #print(resultadoFim)
    if resultadoFim != []:
        return "ERROOOOOOOOOOOOOOOOOOOOOOOOOO"
    else:
        return "AAAAAAAAAAAAAAAA"
    #print(resultadoFim)
    
validaParametroEntreDtInicioDtfimCom("2023/02/03 04:03:03", "2023/02/03 07:03:03")
##UPDATE##

##READ##