# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 14:09:03 2025

@author: PERSONAL
"""
#Importamos una funcion para generar numeros aleatorios 
import random

#Lista de las opciones del juego global
opciones = ["Piedra", "Papel", "Tijera"]

#Contadores para alamcenar los resultados de cada jugada global
jugadas = 0
usuario_gana = 0
pc_gana = 0
empates = 0

#Crear una funcion para el jugador usuario global
def obtener_opcion_usuario():
    """Pide y valida la opción del usuario"""
    while True:
        try:
            eleccion = int(input("Elige un numero: 1 =Piedra, 2 =Papel, 3 =Tijera: ")) - 1
            if eleccion in [0, 1, 2]:
                return eleccion
            else:
                print("Opcion invalida. Intenta de nuevo")
        except ValueError:
            print("Debes ingresar un número de las opciones. Intenta de nuevo")

#Crear una funcion para la computadora
def obtener_opcion_pc():
    """Genera la eleccion de la computadora"""
    return random.randint(0, 2)

#Crear una funcion para determinar al ganador o empate
def determinar_ganador(usuario, pc):
    """Determina quien gana"""
    if usuario == pc:
        return "Empate"
    elif (usuario == 0 and pc == 2) or (usuario == 1 and pc == 0) or (usuario == 2 and pc == 1):
        return "Usuario"
    else:
        return "PC"

#Aqui llamamos a las funciones tanto del usuario como de la PC 
def jugar():
    """Función principal del juego"""
    global jugadas, usuario_gana, pc_gana, empates

    usuario = obtener_opcion_usuario()
    pc = obtener_opcion_pc()
    
    print("Tú elegiste:", opciones[usuario])
    print("La PC eligió:", opciones[pc])

#Aumenta los contadores segun quien gane
    resultado = determinar_ganador(usuario, pc)
    jugadas += 1

    if resultado == "Empate":
        empates += 1
        print("Resultado: Empate")
    elif resultado == "Usuario":
        usuario_gana += 1
        print("Resultado: Ganaste")
    else:
        pc_gana += 1
        print("Resultado: La PC gana")

#Bucle donde muestra la parte final del programa 
while True:
    jugar()
    otra = input("¿Quieres jugar otra vez? (si o no): ").lower()
    if otra != 'si':
        print("Resultados del juego:")
        print("Partidas jugadas:", jugadas)
        print("Victorias del usuario:", usuario_gana)
        print("Victorias de la PC:", pc_gana)
        print("Empates:", empates)
        print("Gracias por jugar")
        break