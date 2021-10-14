
from os import replace


"""ESTA ES LA RAMA DE NIKKO asdasPAPA"""
filename = 'links.txt'

with open(filename) as f_obj:
    prueba = f_obj.read()

print(prueba)

qw = prueba.replace('#' , '!') .replace('file/','#!')
wq=qw 
"""ESTA ES LA RAMA DE NIKKO asdasPAPA"""

print(qw)
