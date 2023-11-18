import crud
import conexao

def validaSalaDisponivel():
    consulta = f'SELECT IDCIRURGIA FROM CIRURGIA'
    conexao.cursor.execute(consulta)
    cirurgiaos = [row[0] for row in conexao.cursor.fetchall()]
    return cirurgiaos

print(str(crud.retorna_Id_ultima_cirurgia()))