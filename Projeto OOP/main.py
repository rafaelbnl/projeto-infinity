from estabelecimento import *
from gerenciador import *
from pessoas import *
from quartos import *

def main():
    print("SISTEMA DE GERENCIAMENTO DE HOTEL")
    
    hotel = Hotel(nome="Refúgio dos Sonhos", logradouro="Rua das Flores", numero=123, rede="Accor")
    print(f"Hotel criado: {hotel.nome}")
    print(f"Endereço: {hotel.logradouro}", {hotel.numero})
    
    print("CRIANDO QUARTOS")
    
    quarto1 = Quarto(101, "single", 150.00, "Livre")
    quarto2 = Quarto(102, "double", 250.00, "Livre")
    quarto3 = Quarto(103, "suite", 400.00, "Livre")
    quarto4 = Quarto(104, "single", 150.00, "Livre")
    
    hotel.cadastrar_quarto(quarto1)
    hotel.cadastrar_quarto(quarto2)
    hotel.cadastrar_quarto(quarto3)
    hotel.cadastrar_quarto(quarto4)
    
    print(f"Total de quartos cadastrados: {len(hotel.lista_de_quartos)}")
    
    gerenciador = Gerenciador_de_reservas(hotel)
    
 
    print("VERIFICANDO DISPONIBILIDADE")
    gerenciador.verificar_disponibilidade()
    
    print("CRIANDO CLIENTES DE TESTE")
    
    cliente1 = Cliente("João Silva", "(11) 98765-4321", "joao@email.com", 1001)
    cliente2 = Cliente("Maria Santos", "(11) 91234-5678", "maria@email.com", 1002)
    
    print(f"Cliente 1: {cliente1.get_nome()} | ID: {cliente1.get_id()}")
    print(f"Cliente 2: {cliente2.get_nome()} | ID: {cliente2.get_id()}")
    
    print("CRIANDO RESERVAS MANUALMENTE")
     
    reserva1 = {
        "cliente": cliente1,
        "quarto": quarto1,
        "dias": 3,
        "valor_total": quarto1.diaria * 3
    }
    
    reserva2 = {
        "cliente": cliente2,
        "quarto": quarto2,
        "dias": 5,
        "valor_total": quarto2.diaria * 5
    }
    
    hotel.lista_de_reservas.append(reserva1)
    hotel.lista_de_reservas.append(reserva2)
    quarto1.status = "Ocupado"
    quarto2.status = "Ocupado"
    
    print(f"Reserva 1: {cliente1.get_nome()} | Quarto {quarto1.numero} | {reserva1['dias']} dias | Total: R${reserva1['valor_total']:.2f}")
    print(f"Reserva 2: {cliente2.get_nome()} | Quarto {quarto2.numero} | {reserva2['dias']} dias | Total: R${reserva2['valor_total']:.2f}")
    
    # Listando reservas
    print("\n" + "=" * 50)
    print("LISTANDO TODAS AS RESERVAS")
    print("=" * 50)
    
    for idx, reserva in enumerate(hotel.lista_de_reservas, 1):
        print(f"\nReserva {idx}:")
        print(f"  Cliente: {reserva['cliente'].get_nome()} (ID: {reserva['cliente'].get_id()})")
        print(f"  Telefone: {reserva['cliente'].get_telefone()}")
        print(f"  Email: {reserva['cliente'].get_email()}")
        print(f"  Quarto: {reserva['quarto'].numero} | Tipo: {reserva['quarto'].tipo.title()}")
        print(f"  Status: {reserva['quarto'].status}")
        print(f"  Dias: {reserva['dias']} | Valor Total: R${reserva['valor_total']:.2f}")
    
    # Verificando disponibilidade após reservas
    print("\n" + "=" * 50)
    print("VERIFICANDO DISPONIBILIDADE APÓS RESERVAS")
    print("=" * 50)
    gerenciador.verificar_disponibilidade()
    
    # Menu interativo
    print("\n" + "=" * 50)
    print("MENU INTERATIVO")
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 50)
        print("OPÇÕES:")
        print("1 - Verificar disponibilidade")
        print("2 - Criar nova reserva")
        print("3 - Modificar reserva existente")
        print("4 - Cancelar reserva")
        print("5 - Listar todas as reservas")
        print("0 - Sair")
        print("-" * 50)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            match opcao:
                case 1:
                    print("\n" + "=" * 50)
                    gerenciador.verificar_disponibilidade()
                    
                case 2:
                    print("\n" + "=" * 50)
                    print("CRIAR NOVA RESERVA")
                    print("=" * 50)
                    gerenciador.criar_reserva()
                    
                case 3:
                    print("\n" + "=" * 50)
                    print("MODIFICAR RESERVA")
                    print("=" * 50)
                    if not hotel.lista_de_reservas:
                        print("Nenhuma reserva cadastrada.")
                    else:
                        print("Reservas cadastradas:")
                        for reserva in hotel.lista_de_reservas:
                            print(f"ID: {reserva['cliente'].get_id()} | Cliente: {reserva['cliente'].get_nome()}")
                        gerenciador.modificar_reserva()
                    
                case 4:
                    print("\n" + "=" * 50)
                    print("CANCELAR RESERVA")
                    print("=" * 50)
                    if not hotel.lista_de_reservas:
                        print("Nenhuma reserva cadastrada.")
                    else:
                        print("Reservas cadastradas:")
                        for reserva in hotel.lista_de_reservas:
                            print(f"ID: {reserva['cliente'].get_id()} | Cliente: {reserva['cliente'].get_nome()}")
                        gerenciador.cancelar_reserva()
                    
                case 5:
                    print("\n" + "=" * 50)
                    print("TODAS AS RESERVAS")
                    print("=" * 50)
                    if not hotel.lista_de_reservas:
                        print("Nenhuma reserva cadastrada.")
                    else:
                        for idx, reserva in enumerate(hotel.lista_de_reservas, 1):
                            print(f"\nReserva {idx}:")
                            print(f"  Cliente: {reserva['cliente'].get_nome()} (ID: {reserva['cliente'].get_id()})")
                            print(f"  Telefone: {reserva['cliente'].get_telefone()}")
                            print(f"  Email: {reserva['cliente'].get_email()}")
                            print(f"  Quarto: {reserva['quarto'].numero} | Tipo: {reserva['quarto'].tipo.title()}")
                            print(f"  Status: {reserva['quarto'].status}")
                            print(f"  Dias: {reserva['dias']} | Valor Total: R${reserva['valor_total']:.2f}")
                    
                case 0:
                    print("\n" + "=" * 50)
                    print("Encerrando sistema...")
                    print("=" * 50)
                    break
                    
                case _:
                    print("\nOpção inválida! Tente novamente.")
                    
        except ValueError:
            print("\nPor favor, digite um número válido.")
        except Exception as e:
            print(f"\nErro: {e}")


print(main())
