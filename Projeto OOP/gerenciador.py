from estabelecimento import *
from pessoas import Cliente
import random


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
        quartos_livres = [q for q in self.hotel.lista_de_quartos if q.status == "Livre"]
        
        if not quartos_livres:
            return "Nenhum quarto disponível no momento."
        
        print("Quartos disponíveis:")
        for quarto in quartos_livres:
            print(f"Quarto {quarto.numero} | Tipo: {quarto.tipo.title()} | Diária: R${quarto.diaria:.2f}")
        
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")
        id_cliente = random.randint(1000, 9999)
        
        cliente = Cliente(nome, telefone, email, id_cliente)
        self.lista_de_hospedes.append(cliente)
        
        numero_quarto = int(input("Digite o número do quarto desejado: "))
        quarto_selecionado = None
        
        for quarto in quartos_livres:
            if quarto.numero == numero_quarto:
                quarto_selecionado = quarto
                break
        
        if not quarto_selecionado:
            return "Quarto não disponível ou não encontrado."
        
        dias = int(input("Digite a quantidade de dias da estadia: "))
        valor_total = quarto_selecionado.diaria * dias
        
        reserva = {
            "cliente": cliente,
            "quarto": quarto_selecionado,
            "dias": dias,
            "valor_total": valor_total
        }
        
        self.hotel.lista_de_reservas.append(reserva)
        quarto_selecionado.status = "Ocupado"
        
        print(f"Reserva criada com sucesso!")
        print(f"Cliente: {cliente.get_nome()} | ID: {cliente.get_id()}")
        print(f"Quarto: {quarto_selecionado.numero} | Valor total: R${valor_total:.2f}")
        
        return "Reserva cadastrada com sucesso."

    def modificar_reserva(self):
        reserva_buscada = int(input("Digite o ID do hóspede: "))
        
        reserva_encontrada = None
        for reserva in self.hotel.lista_de_reservas:
            if reserva["cliente"].get_id() == reserva_buscada:
                reserva_encontrada = reserva
                break
        
        if not reserva_encontrada:
            return "Reserva não encontrada."
        
        cliente = reserva_encontrada["cliente"]
        
        while True:
            print("""
1 - Alterar nome do hóspede
2 - Alterar telefone do hóspede
3 - Alterar e-mail do hóspede
0 - Cancelar alteração
""")
            opt = int(input("Escolha uma opção: "))
            
            match opt:
                case 1:
                    novo_nome = input("Digite o novo nome: ")
                    cliente.set_nome(novo_nome)
                    print("Nome alterado com sucesso!")
                case 2:
                    novo_telefone = input("Digite o novo telefone: ")
                    cliente.set_telefone(novo_telefone)
                    print("Telefone alterado com sucesso!")
                case 3:
                    novo_email = input("Digite o novo e-mail: ")
                    cliente.set_email(novo_email)
                    print("E-mail alterado com sucesso!")
                case 0:
                    print("Alteração cancelada.")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

    def cancelar_reserva(self):
        reserva_buscada = int(input("Digite o ID do hóspede: "))
        
        reserva_encontrada = None
        for reserva in self.hotel.lista_de_reservas:
            if reserva["cliente"].get_id() == reserva_buscada:
                reserva_encontrada = reserva
                break
        
        if not reserva_encontrada:
            return "Reserva não encontrada."
        
        reserva_encontrada["quarto"].status = "Livre"
        
        self.hotel.lista_de_reservas.remove(reserva_encontrada)
        
        print(f"Reserva do cliente {reserva_encontrada['cliente'].get_nome()} cancelada com sucesso!")
        print(f"Quarto {reserva_encontrada['quarto'].numero} liberado.")
        
        return "Reserva cancelada com sucesso."