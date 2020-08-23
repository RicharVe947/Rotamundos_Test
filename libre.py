# -*- coding: utf-8 -*-

from statistics import mean

"""El siguiente problema se estructura en pseudocódigo, siéntase libre de realizar la implementación en el lenguaje deseado.
Favor de publicar su solución en un gist y compartirlo al correo solicitado.
"""
estudiantes ={
    "estudiante1":{
        "Nombre":"Raymundo",
        "Edad":25,
        "Tareas":[90.0, 95, 85.5, 90],
        "Examenes":[75, 65.5, 85]
    },
    "estudiante2":{
        "Nombre":"Aleja",
        "Edad":23,
        "Tareas":[72.0, 89.5, 95, 100],
        "Examenes":[90, 90, 85]
    },
    "estudiante3":{
        "Nombre":"Víctor",
        "Edad":28,
        "Tareas":[95, 80, 100, 0],
        "Examenes":[70, 85, 65]
    }
}
"""Recibe un numero  del 0 al 10 y lo convierte en letras"""
def aletras(num):
    letras={
        "0":"Cero ",
        "1":"Uno ",
        "2":"Dos ",
        "3":"Tres ",
        "4":"Cuatro ",
        "5":"Cinco ",
        "6":"Seis ",
        "7":"Siete ",
        "8":"Ocho ",
        "9":"Nueve ",
        "10":"Diez ",
        ".":"punto "
    }
    letra=""
    for l in str(num):
        letra=letra+letras[l]
    return letra

"""Recibe dos listas de numeros(tareas y promedio) y calcula el promedio de acuerdo a la 
siguiente formula: 20% (promedio tareas) + 80% (promedio exámenes)"""
def promedio(tareas,examenes):
    prom_tarea = mean(tareas)
    prom_exam = mean(examenes)
    return round((prom_tarea*.2 + prom_exam*.8)/10,1)

"""Recibe un nombre de un estudiante y regresa su promedio en letras"""
def score (nombre):
    for line in estudiantes:
        if (estudiantes[line]["Nombre"] == nombre):
            return aletras(promedio(estudiantes[line]["Tareas"],estudiantes[line]["Examenes"]))

"""Calcula el promedio de todos los estudiantes"""
def score_group():
    sum_score=[]
    for line in estudiantes:
        sum_score.append(promedio(estudiantes[line]["Tareas"],estudiantes[line]["Examenes"]))
    return round(mean(sum_score),1)

print (score("Aleja"))
print (score_group())
