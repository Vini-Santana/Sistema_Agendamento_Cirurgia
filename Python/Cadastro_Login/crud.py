import conexao

def createPerfilDeAcesso(senha, usuario, nivel):
    comando = f'INSERT INTO PERFILDEACESSO(SENHA,USUARIO,NIVEL) VALUES ("{senha}","{usuario}",{nivel})'
    conexao.cursor.execute(comando)
    conexao.conexaov.commit()