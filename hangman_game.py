#Juego del ahoracado en consola, sencillo y practico, perdon por la funsión 'Comparation', realmente ni yo sé como funciona
import random
import os
from typing import Dict 

def word_selecition():
    #Con el modulo randon determinamos un numero random que sera la linea de texto de donde sacaremos la palabra que utilizaremos más adelante en el juego
    a=random.randint(1, 354)
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        f= f.readlines()
    word = f[a]
    return word


def normalize(word):
    #Es una función básica para 'tratar' a la palabra que se sacó del archivo txt, quitarle los acentos y las mayusculas 
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b)
        word= word.lower()
        
    return word
            

def dict_generator(palabra):
    #Una vez la plabra ha sido seleccionada y tratada, se crean dos listas: las values y las keys, las values son la palabra desenglosada en letras y las keys es un rango que suma 1 en cada posicion y con eso se puede determinar la posicion de cada letra en la palabra (Puede ser que hayan metodos mucho más sencillos, pero este fue el que se me ocurrió)
    largo=len(palabra)-1
    word= palabra.replace('\n','')
    values_list=list(palabra)
    keys_list=[x for x in range(0,largo+1)]
    #Una vez creadas nuestras dos listas, la funcion dict y zeip se encargan de hacernos un diccionario donde las keys son la posicion de la letra y los values son la letra como tal
    dict_word = dict(zip(keys_list, values_list))

    return dict_word, largo


def comparation(dict, largo):
    #Crea una lista del tamaño de la palabra y lo rellena con '_'
    list=['_']
    list=list*largo
    #Entra a un ciclo while que fuerza al ciclo for a interar varias veces la lista en busca de '_' para determinar si la palabra ha sido completada o no
    x=0
    while x < largo:
        for i in list:
            list_str= ''.join(list)
            if i == '_':
                print(list_str)
                letra=input('Ingresa una letra: ')
                #Pide una letra que va a ser comparada en este cilo for que intera la key y el value del diccionario anteriormente generado para luego determinar si el value es igual a la letra ingresada, entonces elimina el '_' en la posicion de la key y agrega la letra que coinsiden en las posiciones de la key y además suma al cilo while para forzar la interacion del for en la lista varias veces 
                for key,value in dict.items():
                    os.system('cls')
                    if value == letra:
                        list.pop(key)
                        list.insert(key, value)
                        x=x+1
    
    #Dado cierto número de intentos determinados por el algoritmo, se llega al final del ciclo while principal y se pregunta si la lista aún tiene '_', si es así, el usuario ha fallado, sino tiene '_', el usuario a completado el juego exitosamente, además retorna un false, para indicarle al ciclo while del ma funcion run que se detenga
    for i in list:
        if i == '_':
            print('Perdiste, intentalo de nuevo')
            a=False
            break
        else:
            print('Ganaste')
            a=False
            break
    return list, a

    
def run():
    word=word_selecition()
    game_word=normalize(word)
    dict,largo=dict_generator(game_word)
    print('--------------------------------------\nBIENVENIDO AL JUEGO\nENCUENTRA LA PALABRA')
    comprobador=True
    while comprobador == True:
        lista_aciertos,comprobador= comparation(dict, largo)
    print(f'La palabra era: {game_word}')
  

if __name__=='__main__':
    run()