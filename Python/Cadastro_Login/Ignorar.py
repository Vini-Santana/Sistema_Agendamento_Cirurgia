import datetime
import requests
import logging
import crud 
class Log:
    def __init__(self):
        self.time = '' # colocar o nome da equipe fornecida pelo professor - Ex: '4SI_GBD_0X'
        self.senha = ''  # colocar a senha fornecida pelo professor
        self.banco_de_dados = '' # colocar o nome do banco de dados
        self.tabela = '' # colocar uma tabela do banco de dados (definir no método "submit")
        self.chave_primaria = 0 # (definir no método "submit")
        self.crud = '' # CREATE, UPDATE ou DELETE (definir no método "submit")
        self.usuario = '' # Colocar o nome do usuário (definir no método "submit")

    def _insertCmd(self):
        response_statement = 'insert/{your_team, your_password, your_dbname, your_table, your_table_pk, crud, your_username}'
        response_statement = response_statement + f'?&your_team={self.time}'
        response_statement = response_statement + f'&your_password={self.senha}'
        response_statement = response_statement + f'&your_dbname={self.banco_de_dados}'
        response_statement = response_statement + f'&your_table={self.tabela}'
        response_statement = response_statement + f'&your_table_pk={self.chave_primaria}'
        response_statement = response_statement + f'&crud={self.crud}'
        response_statement = response_statement + f'&your_username={self.usuario}'

        insert_cmd = response_statement

        return insert_cmd
    
    def _postRequest(self):

        logging.basicConfig(format='%(levelname)s:%(message)s @ %(asctime)s', level=logging.DEBUG)

        try:
            response = requests.post('http://54.235.63.166:8000/'+self._insertCmd())

            if response.status_code != 200:
                logging.error(f"Resposta={response.__dict__}")
                
            else:
                logging.info(f"Content={response.content}")
                
        except requests.exceptions.RequestException as erro_conexao:
            logging.critical("Error no logging! Tente novamente...")
    
    def submit(self, table, pk, crud, user): # método que inicializa o logging (instanciar)
        '''Método que inicializa o logging (instanciar)'''
        self.tabela = table
        self.chave_primaria = pk
        self.crud = crud
        self.usuario = user
        
        self._postRequest()
crud.update("cirurgia", "status", 2, 2)
##METODO QUE CONVERTE DATA E HORA SEPARADOS PARA DATETIME
#data = "02/05/2023"
#hora = "12:05:12"
#def horario(data, hora):
#    return data + " "+ hora
#
#print(horario(data, hora))
#print(datetime.datetime.strptime(horario(data,hora), '%d/%m/%Y %H:%I:%S'))
#print(datetime.datetime.strftime(datetime.datetime.strptime(horario(data,hora), '%d/%m/%Y %H:%I:%S'),'%d/%m/%Y %H:%I:%S'))
#crud.createCirurgia(datetime.datetime.strptime(horario(data,hora), '%d/%m/%Y %H:%I:%S'), "2023-05-02 10:00:12",1, 1, 1, 1, 1,1 ,1)

#Log.Log.submit(Log, "cirurgia", 25, "CREATE", "ViniV")