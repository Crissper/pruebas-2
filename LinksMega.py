
from os import replace


"""ESTA ES LA RAMA DE NIKKO PAPA"""
filename = 'links.txt'

with open(filename) as f_obj:
    prueba = f_obj.read()

print(prueba)

qw = prueba.replace('#' , '!') .replace('file/','#!')
wq=qw 


print(qw)
