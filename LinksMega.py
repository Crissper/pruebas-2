
from os import replace

filename = 'links.txt'

with open(filename) as f_obj:
    prueba = f_obj.read()

print(prueba)

qw = prueba.replace('#' , '!') .replace('file/','#!')
wq=qw 
""" Este es un comentario multilinea. La
siguiente parte realiza una serie
de cosas muy chulas  EL NIKOO"""
"""asdas"""

print(qw)
