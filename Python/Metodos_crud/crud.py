import conexao

def create(nome_produto, valor):

    # cursor2 = conexao.cursor
    comando = f'INSERT INTO vendas (nome_produto, valor)VALUES ("{nome_produto}", {valor})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()
    #cursorAqui.execute(comando)
    # conexaoAqui.commit()

# conexao.cursor.close()
# conexao.conexaov.close()