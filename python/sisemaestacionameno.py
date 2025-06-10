#Sisema de estacionamento
from datetime import datetime, date
data = date.today()
data_form = data.strftime("%d/%m/%Y")
class SistemaEstacionamento:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity
    def estacionar_veiculo(self, placa_carro):
        agora = datetime.now()
        agora_form = agora.strftime("%d/%m/%Y")
        hora_agora = agora.strftime("%H:%M:%S")
        for i in range(self.capacity):
            if self.slots[i] is None:
                self.slots[i] = placa_carro
                print(f"Veículo de placa: {placa_carro} estacionado na vaga: {i+1} no dia: {data_form} às: {hora_agora}")
                return i+1
        print("Estacionamento cheio! Não possuímos mais vagas.")
        return -1
    def Remover_veiculo(self, vaga):
        agora = datetime.now()
        agora_form = agora.strftime("%d/%m/%Y")
        hora_agora = agora.strftime("%H:%M:%S")
        if vaga < 1 or vaga > self.capacity:
            print("Vaga inexistente.")
            return False
        if self.slots[vaga-1] is None:
            print(f"Vaga de número: {vaga} agora está vazia.")
            return False
        removed_vehicle = self.slots[vaga-1]
        self.slots[vaga-1] = None
        print(f"Veículo de placa: {removed_vehicle} removido da vaga: {vaga} no dia: {data_form} às: {hora_agora}")
        return True
    def get_status(self):
        print("\n📊 S1tatus do estacionamento:")
        print("Vaga Nº.    placa")
        empty = True
        for i, vehicle in enumerate(self.slots, start=1):
            if vehicle is not None:
                print(f"{i:<10} {vehicle}")
                empty = False
        if empty:
            print("Sem veículos estacionados.")
    def payment(self, data_pagamento):
        pagamento = 9
        print(f"realize o pagamento no valor de: R$ {pagamento}")

        while True:
            print (f"Você concorca com o pagamento de R$ {pagamento}")
            forma_pagamento = {'sim': True, 's' : True, 'não': False, 'n': False, '1': True, '2': False}
            concordancia = input("Você concorda com o pagamento? (sim/não): ").lower()
            if concordancia in forma_pagamento:
                if forma_pagamento[concordancia]:
                    print(f"Pagamento realizado com sucesso no dia: {data_form} às: {data_pagamento}.")
                    exit()
                else:
                    print("Pagamento não realizado.")




def main():
    print("Bem-vindo ao Sistema de Estacionamento")
    print("Hoje são:")
    print(data_form)
    capacity = int(input("Digite o total de vagas disponíveis: "))
    sistema_estacionamento = SistemaEstacionamento(capacity)
    while True:
        print("\nEscolha uma opção:")
        print("1. Estacionar veículo")
        print("2. Remover veículo")
        print("3. Mostrar status")
        print("4. Pagar")
        print("5. Sair")

        choice = input("Digite a opção (1-5): ")
        if choice == '1':
            placa_carro = input("Digite a placa do veículo: ")
            sistema_estacionamento.estacionar_veiculo(placa_carro)
        elif choice == '2':
            vaga = int(input("Digite o número da vaga do veículo a ser removido: "))
            sistema_estacionamento.Remover_veiculo(vaga)
        elif choice == '3':
            sistema_estacionamento.get_status()
        elif choice == '4':
            data_pagamento = data
            sistema_estacionamento.payment(data_pagamento)
        elif choice == '5':
            print("Saindo do Sistema de Estacionamento. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, digite 1-5.")
if __name__ == "__main__":
    main()