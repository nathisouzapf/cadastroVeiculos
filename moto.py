from Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas
    
    def __str__(self):
        

        retorno = super().__str__()


        return f'''{retorno}
        - Cilindradas: {self.__cilindradas}'''
    
# Instanciando a classe Moto
falcon= Moto("Honda", "Falcon NX4", "abc", 2005, 400)
# Vai imprimir o retorno do método "__str__()"
print(falcon.__str__())

#Instanciando a classe veículo
cerato = Veiculo("Kia", "Cerato", "IRL", 2011)

print(cerato.__str__())
