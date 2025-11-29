class Pessoa():
    def __init__(self, nome: str, telefone: str, email: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def get_nome(self):
        return self.__nome

    def set_nome(self):
        novo_nome = input("Digite o novo nome a ser cadastrado: ")
        self.__nome = novo_nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self):
        novo_telefone = input("Digite o novo telefone a ser cadastrado: ")
        self.__telefone = novo_telefone

    def get_email(self):
        return self.__email

    def set_email(self):
        novo_email = input("Digite o novo email a ser cadastrado: ")
        self.__email = novo_email

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, id: int):
        super().__init__(nome, telefone, email)
        self.__id = id

    def get_id(self):
        return self.__id
    
    def set_id(self):
        """comentario"""
        return None