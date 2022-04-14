import os
import sys
from collections import OrderedDict

#Abrir lista de cpf
db = "db.txt"
lista =  open(db,'r').readlines()

#Remover reptidos
OrderedDict.fromkeys(lista)
lista = list(OrderedDict.fromkeys(lista))

print(lista)