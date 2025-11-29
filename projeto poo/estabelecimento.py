from quartos import Quarto

class Estabelecimento():
    def __init__(self, nome: str, logradouro: str, numero: int):
        self.nome = nome
        self.logradouro = logradouro
        self.numero = numero

class Hotel(Estabelecimento):
    def __init__(self, nome, logradouro, numero, rede: str):
        super().__init__(nome, logradouro, numero)
        self.rede = rede
        self.lista_de_quartos = []

    def cadastrar_quarto(self):
        numero = int(input("Digite o número do quarto: "))
        tipo = input("Digite o tipo de quarto: ")
        diaria = float(input("Digite o valor da diária do quarto em reais: "))
        status = input("Quarto disponível? (s/n) ").strip().lower()
        if status == "s":
            status = "Livre"
        else:
            status = "Ocupado"

        quarto = Quarto(numero, tipo, diaria, status)
        self.lista_de_quartos.append(quarto)
        return "Quarto cadastrado com sucesso"


    def editar_quarto(self):
        quarto_editado = int(input("Digite o número do quarto que deseja editar: "))
        for quarto in self.lista_de_quartos:
            if quarto.numero == quarto_editado: 
                alterar_diaria = input("Deseja alterar o valor da diária? (s/n) ").strip().lower()
                if alterar_diaria == 's':
                    nova_diaria = float(input("Digite o novo valor da diária: "))
                    quarto.diaria = nova_diaria
                
                alterar_status = input("Deseja alterar o status do quarto? (s/n) ").strip().lower()
                if alterar_status == 's':
                    novo_status = input("Quarto está disponível (s/n)? ").strip().lower()
                    if novo_status == "s":
                        quarto.status = "Livre"
                    else:
                        quarto.status = "Ocupado"
                
                return "Quarto editado com sucesso."
        
        return "Quarto não encontrado." 


    def excluir_quarto(self):
        quarto_excluido = int(input("Digite o número do quarto a excluir: "))
        for quarto in self.lista_de_quartos:
            if quarto.numero == quarto_excluido:
                self.lista_de_quartos.remove(quarto)
                return "Quarto excluído com sucesso."
        
        return "Quarto não encontrado."

    def exibir_quartos(self):
        if not self.lista_de_quartos:
            return "Nenhum quarto cadastrado."
        
        for quarto in self.lista_de_quartos:
            print(f"Quarto {quarto.numero} | Tipo: {quarto.tipo.title()} | Diária: R${quarto.diaria:.2f} | Status: {quarto.status}")
        
        return None
