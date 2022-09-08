from calendar import c
from functools import reduce
from operator import truediv
import random
from re import X
from typing import Dict 

def word_selecition():
    a=random.randint(1, 354)
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        f= f.readlines()
    word = f[a]
    return word

def normalize(word):
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
    largo=len(palabra)-1
    palabra= palabra.replace('\n','')
    values_list=list(palabra)
    keys_list=[x for x in range(0,largo+1)]
    dict_word = dict(zip(keys_list, values_list))
    print(dict_word)    

    return dict_word, largo


def comparation(dict, largo):
    list=['_']
    list=list*largo
    x=0
    while x < largo:
        for i in list:
            list_str= ''.join(list)
            print(list_str)
            if i == '_':
                letra=input('Ingrese una letra: ')
                for key,value in dict.items():
                    if value == letra:
                        list.pop(key)
                        list.insert(key, value)
                        x=x+1
    print(list) 
    print('palara encontrada')
                   
    return list


    
def run():
    word=word_selecition()
    game_word=normalize(word)
    print(game_word)
    dict,largo=dict_generator(game_word)
    lista_aciertos= comparation(dict, largo)
    

   

if __name__=='__main__':
    run()