import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='cirurgia',
)

cursor = conexao.cursor()

#CREAT
# nome_produto = "computador"
# valor = 100
# comando = f'INSERT INTO vendas (nome_produto, valor)VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit()
#
#id = 4
#data = "STR_TO_DATE('1900-10-04 22:23:00', '%Y-%m-%d %k:%i:%s')"
#comando = f'INSERT INTO testeData (id, dataCirurgia) VALUES ("{id}", {data})'
#cursor.execute(comando)
#conexao.commit()

# READ
comando_read = 'SELECT * FROM vendas'
cursor.execute(comando_read)
resultado = cursor.fetchall()
print(resultado)


# UPDATE
# valor = 100
# coluna = "valor"
# idVendas = 5
# comando = f'UPDATE vendas SET {coluna} = {valor} where idVendas = {idVendas}'
# cursor.execute(comando)
# conexao.commit()

# DELETE
# idVendas = 9
# comando_delete = f'DELETE FROM vendas where idVendas = {idVendas}'
# cursor.execute(comando_delete)
# conexao.commit()


cursor.close()
conexao.close()
