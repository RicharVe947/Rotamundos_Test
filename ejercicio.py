# -*- coding: utf-8 -*-

""" Hacer una función llamada "separador" que me regrese:
 ¿Cuántas letras mayúsculas hay en el string "source"?
 ¿Cuántas letras minúsculas hay en el string "source"?
 ¿Cuántos símbolos hay en el string "source"? """

"""Regreasa una lista con el numero de letras mayusculas, minusculas y simbolos"""
def separador(source):
    mayus = 0
    minus = 0
    simbo = 0

    for l in source:
        if (l >= 'a' and l <= 'z' or l in "áéíóúñ"):
            minus = minus + 1
        elif (l >= 'A' and l <= 'Z' or l in 'ÁÉÍÓÚÑ'):
            mayus = mayus + 1
        else:
            simbo = simbo +1
    return mayus,minus,simbo


source = "P@#yn26at^&i5ve"
mayus,minus,simbo = separador(source)
print ("Mayúsculas: ",mayus," Minúsculas: ",minus," Símbolos: ",simbo)
