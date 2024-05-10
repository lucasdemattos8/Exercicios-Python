class CaixaEletronico():
    def __init__(self, nomeUsuario : str, depositoInicial : float):
        self.nomeUsuario = nomeUsuario
        self.saldo = depositoInicial

    def saque(self, valorParaSaque : float):
        """Método para saque de saldo do usuário."""
        if valorParaSaque <= 0:
            print("="*50)
            print("[FALHA] O saque não foi realizado com sucesso.")
            print("Valor inserido inválido!")
            input("\nPressioner ENTER para sair: ")
        elif valorParaSaque <= self.saldo:
            self.saldo -= valorParaSaque
            print("="*50)
            print("[SUCESSO] Saque realizado com sucesso.")
            input("\nPressioner ENTER para sair: ")
        else:
            print("="*50)
            print("[FALHA] O saque não foi realizado com sucesso.")
            print(f"Falta um total de R$ {valorParaSaque - self.saldo:.2f}.")
            input("\nPressioner ENTER para sair: ")
    
    def deposito(self, valorParaDeposito : float):
        """Método para deposito de saldo na conta do usuário."""
        if valorParaDeposito <= 0:
            print("="*50)
            print("[FALHA] O deposito não foi realizado com sucesso.")
            print("Valor inserido inválido!")
            input("\nPressioner ENTER para sair: ")
        else:
            self.saldo += valorParaDeposito
            print("="*50)
            print("[SUCESSO] Deposito realizado com sucesso.")
            input("\nPressioner ENTER para sair: ")

    def verificarSaldo(self):
        """Método para verificar o saldo na conta do usuário"""
        print("="*50)
        print(f"[SISTEMA] Você tem R$ {self.saldo:.2f} de saldo.")
        input("\nPressioner ENTER para sair: ")

# Loop de repetição (Cadastro Usuário)

nomeUsuario = input("Insira seu nome: ")
while True:
    escolha = input("Você deseja fazer um deposito inicial (Y / N): ")

    if escolha.upper() == "Y":
        depositoInicial = float(input("Insira o seu deposito inicial R$ "))
        if depositoInicial <= 0:
            print("="*50)
            print("[FALHA] O deposito não foi realizado com sucesso.")
            print("Valor inserido inválido.")
            input("\nPressioner ENTER para sair: ")
        else:
            break
    elif escolha.upper() == "N":
        depositoInicial = 0
        break
    else:
        print("="*50)
        print("[SISTEMA] Escolha INVÁLIDA!")

usuario = CaixaEletronico(nomeUsuario, depositoInicial)

escolha = 10

try:
    while escolha != 0:
        print("\n\n")
        print("="*20)
        print("")
        print("Caixa eletrônico")
        print()
        print("="*20)
        print("1 - Verificar saldo;")
        print("2 - Saque;")
        print("3 - Deposito;")
        print("0 - Sair.")
        print("")
        escolha = int(input("Insira a sua opção: "))
        if escolha == 1:
            usuario.verificarSaldo()
        elif escolha == 2:
            print("="*50)
            valorParaSaque = float(input("Insira um valor para saque R$ "))
            usuario.saque(valorParaSaque)
        elif escolha == 3:
            print("="*50)
            valorParaDeposito = float(input("Insira um valor para deposito R$ "))
            usuario.deposito(valorParaDeposito)
        elif escolha == 0:
            break
except ValueError:
    escolha = 10

print("[SISTEMA] Obrigado por utilizar nosso caixa eletrônico!")
