#!/usr/bin/python3

fd = open('/etc/passwd', 'r')
lineas = fd.readlines()

lineas[:1] # ['pepepepepeppepe\n']
lineas[0] # 'pepepepepeppepe\n'

for linea in lineas:
#    print(linea)
    pos_fin = linea.find(':')
    login = linea[:pos_fin]
    pos_com = linea.rfind(':')
#    print(pos_com)
    shell = linea[pos_com+1:-1]
    print(login, shell)

for linea in lineas:
    elementos = linea.split(':')
#    print(elementos)
    login = elementos[0]
    shell = elementos[-1]
    shell_bueno = shell[:-1]
    print(login, shell_bueno)

for linea in lineas:
    login = linea.split(':')[0]
    shell = linea.split(':')[-1][:-1]
    print(login, shell)

