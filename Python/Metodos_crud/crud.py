import conexao

def create(nome_produto, valor):
    comando = f'INSERT INTO vendas (nome_produto, valor)VALUES ("{nome_produto}", {valor})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

def createTesteData(id, data):
    comando = f'INSERT INTO testeData (id, dataCirurgia) VALUES ("{id}", str_to_date("{data}", "%Y-%m-%d %k:%i:%s"))'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()

