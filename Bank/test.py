from models.cliente import Cliente
from models.conta import Conta

carrie: Cliente = Cliente('Carrie Fisher', '123.456.789-00', '21/10/1956')
mark: Cliente = Cliente('Mark Hamill', '456.987.321.11', '25/09/1951')

print(carrie)
print(mark)

conta_carrie: Conta = Conta(carrie)
conta_mark: Conta = Conta(mark)

print(conta_carrie)
print(conta_mark)
