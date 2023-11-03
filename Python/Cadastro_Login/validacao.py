import conexao

def validaUsuarioSenha_RetornaNivelAcesso(usuario, senha):
     
    consulta = f'SELECT SENHA FROM PERFILDEACESSO WHERE USUARIO = "{usuario}"'
    conexao.cursor.execute(consulta)
    resultadoFim = conexao.cursor.fetchall()    
    if resultadoFim == [] or senha != resultadoFim[0][0]:
        raise ValueError("Usuário ou senha incorretos")
    else:
        return True
    
