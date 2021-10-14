
from os import replace


filename = 'links.txt'

with open(filename) as f_obj:
    prueba = f_obj.read()

print(prueba)

qw = prueba.replace('#' , '!') .replace('file/','#!')
asd

print(qw)
