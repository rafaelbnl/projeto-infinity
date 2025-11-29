from estabelecimento import Hotel
from gerenciador import Gerenciador_de_reservas

hotel1 = Hotel(nome="EZ Aldeota", logradouro="Rua Nunes Valente", numero=1560, rede="Accor")

hotel1.cadastrar_quarto()

gerenciador = Gerenciador_de_reservas(hotel1)

gerenciador.verificador_disponibilidade()

print(f"Total de quartos: {len(gerenciador.hotel.lista_de_quartos)}")