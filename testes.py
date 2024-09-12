from Veiculo import Veiculo
from moto import Moto

# Instanciando a classe Moto
falcon= Moto("Honda", "Falcon NX4", "abc", 2005, 400)
# Vai imprimir o retorno do método "__str__()"
print(falcon.__str__())

#Instanciando a classe veículo
cerato = Veiculo("Kia", "Cerato", "IRL", 2011)

print(cerato.__str__())
