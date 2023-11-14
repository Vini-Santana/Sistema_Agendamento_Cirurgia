# Feito por Eduardo, Caio, Lucas, Gabriel, Nicolas e Olivia
# Código baseado na documentação do Projeto Integrador de Redes de Computadores modificado

# Feito por Eduardo, Caio, Lucas, Gabriel, Nicolas e Olivia
# Código baseado na documentação do Projeto Integrador de Redes de Computadores modificado

import requests
import logging

class Log:
    def __init__(self):
        self.time = '4SI_GBD_04' # colocar o nome da equipe fornecida pelo professor - Ex: '4SI_GBD_0X'
        self.senha = 'ChYFeao3zW'  # colocar a senha fornecida pelo professor
        self.banco_de_dados = 'cirurgiaDB' # colocar o nome do banco de dados
        self.tabela = 'cirurgia' # colocar uma tabela do banco de dados (definir no método "submit")
        self.chave_primaria = 25 # (definir no método "submit")
        self.crud = 'CREATE' # CREATE, UPDATE ou DELETE (definir no método "submit")
        self.usuario = 'ViniciusV' # Colocar o nome do usuário (definir no método "submit")

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