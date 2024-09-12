from carro import Carro
from moto import Moto
from caminhao import Caminhao

import os
os.system('cls')

from Veiculo import Veiculo

listaVeiculos = [
    Carro("Hyundai", "HB20", "ABC", 2023, 4),
    Moto("Yamaha", "Lander", "DEF", 2008, 250),
    Caminhao("Mercedes", "Accelo", "GHI", 2014, 13000)
]

def cadastrar():
    os.system('cls')
    print("Qual o tipo de veículo: (1) Carro - (2) Moto - (3) Caminhão")
    tipo = input()
    print("Digite a marca: ")
    marca = input()
    print("Digite o modelo:")
    modelo = input()
    print("Digite a placa: ")
    placa = input()
    print("Digite o ano:")
    ano = input()
    if tipo == "1":
        print("Digite o número de portas: ")
        nPortas = input()
        veiculoAdd = Carro(marca, modelo, placa, ano, nPortas)
    elif tipo == "2":
        print("Digite as cilindradas: ")
        cilindradas = input()
        veiculoAdd = Moto(marca, modelo, placa, ano, cilindradas)
    elif tipo == "3":
        print("Digite a capacidade do caminhão: ")
        capacidade = input()
        veiculoAdd = Caminhao(marca, modelo, placa, ano, capacidade)
    listaVeiculos.append(veiculoAdd)

def listar():
    os.system('cls')
    if len(listaVeiculos) == 0:
        print("Não existem veículos cadastrados.")
    else:
        i = 1 
        for veiculo in listaVeiculos:
            print(f"Veículo: {i}")
            print(f" {veiculo}")
            i += 1 
    input()

def excluir():
    listar()
    print("Digite a placa que deseja exluir")
    placa = input()
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo.get_placa() == placa:
            listaVeiculos.remove(veiculo)
            encontrou = True
            break
    if encontrou:
        print("Veículo excluído")
    else: 
        print("Veículo não encontrado")


while True:
    os.system('cls')
    print("Escolha uma das opções")
    print("1 - Cadastrar Veículos")
    print("2 - Listar Veículos")
    print("3 - Excluir Veículo")
    print("0 - SAIR")

    opcao = input()
    try: 
        opcao = int(opcao) 
    except:
        print("Opção Inválida")


    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    elif opcao == 0:
        break
    else:
        print("Opcao Inválida")