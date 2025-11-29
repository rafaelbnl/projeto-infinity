from estabelecimento import *

class Gerenciador_de_reservas():
    def __init__(self, hotel):
        self.hotel = hotel
        self.lista_de_hospedes = []

    def verificar_disponibilidade(self):
        quartos_livres = [q for q in self.hotel.lista_de_quartos if q.status == "Livre"]
        
        if not quartos_livres:
            return "Nenhum quarto disponível no momento."
        
        print("Quartos disponíveis:")
        for quarto in quartos_livres:
            print(f"Quarto {quarto.numero} | Tipo: {quarto.tipo.title()} | Diária: R${quarto.diaria:.2f}")
        
        return None
    

    def criar_reserva(self):
        hospede = input("Digite o nome do hóspede: ")
        telefone = input("Digite o telefone do hóspede: ")
        email = input("Digite o e-mail do hóspede: ")
        import random
        novo_id = random.randint(1, 1_000_000)
        while novo_id in self.lista_de_ids:
            novo_id = random.randint(1, 1_000_000)
        quarto_reservado = int(input("Digite o número do quarto: "))
        self.lista_de_hospedes.append({"Nome": hospede, "ID": novo_id, "Telefone": telefone, "E-mail": email })
        return f"Reserva criada para o hóspede {hospede}; ID: {novo_id}"